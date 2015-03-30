from mrjob.job import MRJob
from mrjob.step import MRStep
import urllib2
from operator import itemgetter
import os


class WikiStatsMapper(MRJob):

    def init_wiki(self):
        self.dictionary_size = 5000

    def title_test(self, sanatized):
        for character in '^.&,;:\'?%#~@':
            sanatized = sanatized.replace(character, '').lower()
        # replace white space and such with underline for consitent results
        for special in ['%20', '+', "-"]:
            sanatized = sanatized.replace(special, '_')
        # force remaining html code to regular ascii
        sanatized = urllib2.unquote(sanatized)
        # convert to utf and back to ascii in order to remove accents
        sanatized = sanatized.decode('ascii', 'ignore')
        sanatized = sanatized.encode('ascii', 'ignore')
        # Final pass:
        for special in ["__"]:
            sanatized = sanatized.replace(special, '_')
        # Some final filters
        ignore_list = [':User:', 'Image:', 'Special:',
                       'Main_Page', '_._', 'Wiki', '%s', 'index.html']
        if any([i in sanatized for i in ignore_list]) or sanatized == \
                'Search' or sanatized == '_' or sanatized == '':
            return False
        else:
            self.title = sanatized
            return True

    def count_test(self, number):
        try:
            self.counter = int(number)
            return True
        except ValueError:
            return False

    def wiki_mapper(self, _, line):
        # We are restricting ourselves to the English version
        # discard if there is somehow a typo (this data looks good though)
        # throwing out very long titles too
        # Finally, there are a ton of entries with pagecount 1
        # We can save time by not piping them out, since we are looking for
        # the top hits; we could be even more restrictive to save time;
        # also, the single hits might be from a crawler of some sort anyway

        #if os.environ['WANTED_FILE'] in os.environ["map_input_file"]:
        try:
            line = line.strip().split()
            if line[0] == "en" and self.count_test(line[2]) and \
                    self.title_test(line[1]) and self.counter > 1:
                yield (self.title, self.counter)
        except:
            pass

   # Reducer
    def wiki_reducer(self, key, values):
        yield None, (key, sum(values))

    def get_top_hits(self, _, wiki_count_pair):
        try:
            final_list = sorted(wiki_count_pair, key=lambda x: x[1],
                                reverse=True)[:self.dictionary_size]
        except:
            final_list = wiki_count_pair
        for i in final_list:
            key, values = i
            key = key.replace('"', '')
            yield key, values

    def steps(self):
        return [
            MRStep(mapper_init=self.init_wiki,
                   mapper=self.wiki_mapper,
                   reducer=self.wiki_reducer),
            MRStep(reducer_init=self.init_wiki,
                   reducer=self.get_top_hits)
        ]


if __name__ == '__main__':
    WikiStatsMapper.run()

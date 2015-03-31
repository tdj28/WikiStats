name "wikistats"

run_list(
    "recipe[chef-solo-search]",
    "recipe[wikistats::default]", 
    "recipe[wikistats::mysql]",
    "recipe[wikistats::python]",
    "recipe[wikistats::web]"
)

name "wikistats"

run_list(
    "recipe[chef-solo-search]",
    "recipe[wikistats::default]",
    "recipe[wikistats::web]"
)

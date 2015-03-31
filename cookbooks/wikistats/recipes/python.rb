include_recipe "python"

pips = [
    "flask",
    "redis",
    "nose",
    "mock",
    "flask-mysql"
]

pips.each do |p|
    python_pip p do
        action :install
    end
end


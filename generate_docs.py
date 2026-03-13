import os
import sys

from pydoc_markdown.interfaces import Context, Resolver
from pydoc_markdown.contrib.loaders.python import PythonLoader
from pydoc_markdown.contrib.processors.crossref import CrossrefProcessor
from pydoc_markdown.contrib.processors.filter import FilterProcessor
from pydoc_markdown.contrib.processors.smart import SmartProcessor
from pydoc_markdown.contrib.renderers.markdown import MarkdownRenderer


class ReferenceResolver(Resolver):

    def __init__(self):
        self.references = {}

    def resolve_ref(self, scope, ref):
        return self.references.get(ref)

resolver = ReferenceResolver()

context = Context(directory=".")
loader = PythonLoader(search_path=["src"])
filter = FilterProcessor(expression="not name.startswith(\"_\")")
smart = SmartProcessor()
processor = CrossrefProcessor()
renderer = MarkdownRenderer(
    filename="docs.md",
    render_toc=True,
    descriptive_class_title=False,
    descriptive_module_title=True,
    use_fixed_header_levels=False,
    # header_level_by_type=,
)

loader.init(context)
filter.init(context)
smart.init(context)
processor.init(context)
renderer.init(context)

modules = [m for m in loader.load()]

for module in modules:
    module.members = [m for m in module.members if not hasattr(m, "target") and not m.name.startswith("_")]
    for member in module.members:
        resolver.references[member.name] = f"#{module.name}.{member.name}"
        if hasattr(member, "members"):
            for m in member.members:
                resolver.references[f"{member.name}.{m.name}"] = f"#{module.name}.{member.name}.{m.name}"

filter.process(modules, resolver)
smart.process(modules, resolver)
processor.process(modules, resolver)

old_file = ""
if os.path.exists("docs.md"):
    with open("docs.md", "r") as f:
        old_file = f.read()

renderer.render(modules)

new_file = ""
with open("docs.md", "r") as f:
    new_file = f.read()

if new_file != old_file:
    sys.exit(1)

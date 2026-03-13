from pydoc_markdown.interfaces import Context, Resolver
from pydoc_markdown.contrib.loaders.python import PythonLoader
from pydoc_markdown.contrib.processors.crossref import CrossrefProcessor
from pydoc_markdown.contrib.processors.filter import FilterProcessor
from pydoc_markdown.contrib.renderers.markdown import MarkdownRenderer

class ReferenceResolver(Resolver):

    def __init__(self):
        self.references = {}

    def resolve_ref(self, scope, ref):
        # print(ref)
        # print(self.references[ref])
        return self.references.get(ref)

resolver = ReferenceResolver()

context = Context(directory=".")
loader = PythonLoader(search_path=["src"])
processor = CrossrefProcessor()
filter = FilterProcessor(expression="not name.startswith(\"_\")")
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
processor.init(context)
renderer.init(context)

modules = [m for m in loader.load()]

for module in modules:
    module.members = [m for m in module.members if not hasattr(m, "target") and not m.name.startswith("_")]
    for member in module.members:
        resolver.references[member.name] = f"#{module.name}.{member.name}"

filter.process(modules, resolver)
processor.process(modules, resolver)

renderer.render(modules)
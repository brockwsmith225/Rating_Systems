from pydoc_markdown.interfaces import Context, Resolver
from pydoc_markdown.contrib.loaders.python import PythonLoader
from pydoc_markdown.contrib.processors.crossref import CrossrefProcessor
from pydoc_markdown.contrib.renderers.markdown import MarkdownRenderer

class ReferenceResolver(Resolver):

    def __init__(self):
        self.references = {}

    def resolve_ref(self, scope, ref):
        print(ref)
        print(self.references[ref])
        return self.references.get(ref)

resolver = ReferenceResolver()

context = Context(directory=".")
loader = PythonLoader(search_path=["src"])
processor = CrossrefProcessor()
renderer = MarkdownRenderer(filename="docs.md", render_module_header=False)

loader.init(context)
processor.init(context)
renderer.init(context)

modules = [m for m in loader.load()]

for module in modules:
    module.members = [m for m in module.members if not hasattr(m, "target")]
    for member in module.members:
        resolver.references[member.name] = f"{module.name}.{member.name}"

processor.process(modules, resolver)

renderer.render(modules)
from clip_annot_post import clip
from typing import get_type_hints
import inspect

print(clip.__annotations__)
print(get_type_hints(clip))
print(inspect.get_annotations(clip))
inspect.getinnerframes


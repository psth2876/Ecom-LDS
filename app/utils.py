from django.utils.text import slugify
import uuid

def generate_new_slug(klass,title):
    slug = slugify(title)
    model_class = klass.objects.filter(slug=slug)
    if model_class.exists():
        random_string = str(uuid.uuid4()).split("-")[0]
        new_slug = slug+f"-{random_string}"
        return new_slug
    return slug
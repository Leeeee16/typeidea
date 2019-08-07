from dal import autocomplete

from blog.models import Category, Tag


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # 先判断如果是未登录用户，直接返回空queryset
        if not self.request.user.is_authenticated():
            return Category.objects.none()

        # 获取该用户创建的所有分类
        qs = Category.objects.filter(owner=self.request.user)

        # 判读是否存在q，q为url参数上传递来的值
        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()

        qs = Tag.objects.filter(owner=self.request.user)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

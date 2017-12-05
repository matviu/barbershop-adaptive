from django.contrib import admin
from .models import Review
from .models import ReviewPhoto


class InlineReviewPhoto(admin.StackedInline):
	model = ReviewPhoto
	extra = 1


class ReviewAdmin(admin.ModelAdmin):
	inlines = [
		InlineReviewPhoto,
	]


admin.site.register(Review, ReviewAdmin)

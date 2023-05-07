from rest_framework.fields import SerializerMethodField, BooleanField, IntegerField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models import Ad, Category, Selection
from ads.validators import check_not_true
from users.models import User
from users.serializers import UserSerializer


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(ModelSerializer):
    is_published = BooleanField(validators=[check_not_true], required=False)
    age = IntegerField(read_only=True)

    class Meta:
        model = Ad
        fields = "__all__"


class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        exclude = ("description",)
        model = Ad


class AdAuthorSerializer(ModelSerializer):
    total_ads = SerializerMethodField()

    def get_total_ads(self, obj):
        return obj.ad_set.count()

    class Meta:
        exclude = ("password", "role")
        model = User


class AdDetailSerializer(ModelSerializer):
    author = UserSerializer()
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"


###############################

class SelectionSerializer(ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field="username", required=False, read_only=True)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["owner"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionListSerializer(ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionDetailSerializer(ModelSerializer):
    items = AdSerializer(many=True)
    owner = SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Selection
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

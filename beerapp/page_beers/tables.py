import django_tables2 as tables
from beerapp.db_models.t_beers.models import BeerApp
from django_tables2.utils import A

class BeerTable(tables.Table):
    beername=tables.LinkColumn('beer_detail',args=[A('pk')])

    class Meta:
        model=BeerApp
        template_name = 'django_tables2/semantic.html'
        exclude=['beerid', 'beer_img_name','comments']
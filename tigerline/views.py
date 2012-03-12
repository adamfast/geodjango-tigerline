from django.conf import settings
from django.contrib.gis.maps.google import GoogleMap
from django.contrib.gis.maps.google.overlays import GMarker, GEvent, GPolyline, GPolygon
from django.shortcuts import get_object_or_404, render_to_response
from models import Zipcode


def zipcode_detail(request, object_id):
    zipcode = get_object_or_404(Zipcode, code=object_id)

    polygons = ()

    polygons += (GPolygon(zipcode.mpoly),)

    return render_to_response('census/zipcode_detail.html', {
        'google': GoogleMap(key=settings.GOOGLE_MAPS_API_KEY, polygons=polygons),
        'object': zipcode,
    })

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from airport.views import (
    CrewViewSet,
    AirportViewSet,
    TicketViewSet,
    RouteViewSet,
    AirplaneTypeViewSet,
    AirplaneViewSet,
    FlightViewSet,
    OrderViewSet
)

router = DefaultRouter()
router.register("crew", CrewViewSet)
router.register("airport", AirportViewSet)
router.register("route", RouteViewSet)
router.register("airplaneType", AirplaneTypeViewSet)
router.register("airplane", AirplaneViewSet)
router.register("flight", FlightViewSet)
router.register("order", OrderViewSet)
router.register("ticket", TicketViewSet)


urlpatterns = [path("", include(router.urls))]

app_name = "airport"

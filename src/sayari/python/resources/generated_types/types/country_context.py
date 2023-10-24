# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CountryContext(str, enum.Enum):
    CITIZENSHIP = "citizenship"
    INCORPORATION = "incorporation"
    RESIDENCE = "residence"
    NATIONALITY = "nationality"
    ADDRESS = "address"
    VESSEL_FLAG = "vessel_flag"
    DOMICILE = "domicile"
    SHIPMENT_DEPARTURE = "shipment_departure"
    SHIPMENT_ARRIVAL = "shipment_arrival"
    SHIPMENT_TRANSIT = "shipment_transit"
    ACTIVITY_IN = "activity_in"
    MENTIONED_IN = "mentioned_in"

    def visit(
        self,
        citizenship: typing.Callable[[], T_Result],
        incorporation: typing.Callable[[], T_Result],
        residence: typing.Callable[[], T_Result],
        nationality: typing.Callable[[], T_Result],
        address: typing.Callable[[], T_Result],
        vessel_flag: typing.Callable[[], T_Result],
        domicile: typing.Callable[[], T_Result],
        shipment_departure: typing.Callable[[], T_Result],
        shipment_arrival: typing.Callable[[], T_Result],
        shipment_transit: typing.Callable[[], T_Result],
        activity_in: typing.Callable[[], T_Result],
        mentioned_in: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CountryContext.CITIZENSHIP:
            return citizenship()
        if self is CountryContext.INCORPORATION:
            return incorporation()
        if self is CountryContext.RESIDENCE:
            return residence()
        if self is CountryContext.NATIONALITY:
            return nationality()
        if self is CountryContext.ADDRESS:
            return address()
        if self is CountryContext.VESSEL_FLAG:
            return vessel_flag()
        if self is CountryContext.DOMICILE:
            return domicile()
        if self is CountryContext.SHIPMENT_DEPARTURE:
            return shipment_departure()
        if self is CountryContext.SHIPMENT_ARRIVAL:
            return shipment_arrival()
        if self is CountryContext.SHIPMENT_TRANSIT:
            return shipment_transit()
        if self is CountryContext.ACTIVITY_IN:
            return activity_in()
        if self is CountryContext.MENTIONED_IN:
            return mentioned_in()

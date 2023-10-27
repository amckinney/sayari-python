# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BusinessPurposeStandard(str, enum.Enum):
    """
    Business purpose standard enums describe the type of code listed in a business purpose attribute, which may or may not allow for Pyisic conversions/lookups.
    """

    CNAE_2 = "CNAE2"
    """
    Classificação Nacional de Atividades Econômicas - Brazil National Economic Activity Classification, Rev. 2.0
    """

    ISIC_3 = "ISIC3"
    """
    International Standard Industrial Classification, Rev. 3
    """

    ISIC_31 = "ISIC31"
    """
    International Standard Industrial Classification, Rev. 3.1
    """

    ISIC_4 = "ISIC4"
    """
    International Standard Industrial Classification, Rev. 4
    """

    JSIC_13 = "JSIC13"
    """
    Japan Standard Industrial Classification, Rev. 13
    """

    KSIC_10 = "KSIC10"
    """
    Korean Standard Industry Classification, Rev. 10
    """

    NACE_1 = "NACE1"
    """
    Nomenclature of Economic Activities, Rev. 1
    """

    NACE_2 = "NACE2"
    """
    Nomenclature of Economic Activities, Rev. 2
    """

    NAICS_2017 = "NAICS2017"
    """
    North American Industry Classification System, Rev. 2017
    """

    SKD_2002 = "SKD2002"
    """
    Standardna klasifikacija dejavnosti - Slovenia Standard Classification of Activities, Rev. 2002
    """

    SKD_2008 = "SKD2008"
    """
    Standardna klasifikacija dejavnosti - Slovenia Standard Classification of Activities, Rev. 2008
    """

    TSIC_2552 = "TSIC2552"
    """
    การจัดประเภทมาตรฐานอุตสาหกรรมประเทศไทย ปี 2552 - Thailand Standard Industrial Classification, Rev. 2009
    """

    NACEBEL_2003 = "NACEBEL2003"
    """
    Nomenclature des activités économiques - Belgium Nomenclature of Economic Activities, Rev. 2003
    """

    NACEBEL_2008 = "NACEBEL2008"
    """
    Nomenclature des activités économiques - Belgium Nomenclature of Economic Activities, Rev. 2008
    """

    NAF_1 = "NAF1"
    """
    Nomenclature d'activités française - French Nomenclature of Economic Activities, Rev. 1
    """

    NAF_2 = "NAF2"
    """
    Nomenclature d'activités française - French Nomenclature of Economic Activities, Rev. 2
    """

    GCED_2011 = "GCED2011"
    """
    Экономикалык Ишмердиктердин Тyрлөрүнүн Мамлекеттик Классификатору - Kyrgyz State Economic Activity Classification, Rev. 2011
    """

    SCIAN_2018 = "SCIAN2018"
    """
    Sistema de Clasificación Industrial de América del Norte - Mexico North American Industry Classification System, Rev. 2018
    """

    CCNAE_2021 = "CCNAE2021"
    """
    Clasificador Nacional de Actividades Económicas(CNAE) - Cuba National Economic Activity Classifications, Rev. 2021
    """

    CAEM_2005 = "CAEM2005"
    """
    Clasificatorul Activităţilor Din Economia Moldovei - Moldova Classification of Economic Activities, Rev. 2005
    """

    SBI_2008 = "SBI2008"
    """
    De Standaard Bedrijfsindeling (SBI) - Netherlands Standard Company Classification, Rev. 2008
    """

    HS = "HS"
    """
    Harmonized System Codes (standardized numerical method of classifying traded products)
    """

    SIC = "SIC"
    """
    Standard Industrial Classification (SIC) Code List (USA)
    """

    SSIC_2020 = "SSIC2020"
    """
    Singapore Standard Industrial Classification (national standard for classifying economic activities undertaken by economic units)
    """

    def visit(
        self,
        cnae_2: typing.Callable[[], T_Result],
        isic_3: typing.Callable[[], T_Result],
        isic_31: typing.Callable[[], T_Result],
        isic_4: typing.Callable[[], T_Result],
        jsic_13: typing.Callable[[], T_Result],
        ksic_10: typing.Callable[[], T_Result],
        nace_1: typing.Callable[[], T_Result],
        nace_2: typing.Callable[[], T_Result],
        naics_2017: typing.Callable[[], T_Result],
        skd_2002: typing.Callable[[], T_Result],
        skd_2008: typing.Callable[[], T_Result],
        tsic_2552: typing.Callable[[], T_Result],
        nacebel_2003: typing.Callable[[], T_Result],
        nacebel_2008: typing.Callable[[], T_Result],
        naf_1: typing.Callable[[], T_Result],
        naf_2: typing.Callable[[], T_Result],
        gced_2011: typing.Callable[[], T_Result],
        scian_2018: typing.Callable[[], T_Result],
        ccnae_2021: typing.Callable[[], T_Result],
        caem_2005: typing.Callable[[], T_Result],
        sbi_2008: typing.Callable[[], T_Result],
        hs: typing.Callable[[], T_Result],
        sic: typing.Callable[[], T_Result],
        ssic_2020: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BusinessPurposeStandard.CNAE_2:
            return cnae_2()
        if self is BusinessPurposeStandard.ISIC_3:
            return isic_3()
        if self is BusinessPurposeStandard.ISIC_31:
            return isic_31()
        if self is BusinessPurposeStandard.ISIC_4:
            return isic_4()
        if self is BusinessPurposeStandard.JSIC_13:
            return jsic_13()
        if self is BusinessPurposeStandard.KSIC_10:
            return ksic_10()
        if self is BusinessPurposeStandard.NACE_1:
            return nace_1()
        if self is BusinessPurposeStandard.NACE_2:
            return nace_2()
        if self is BusinessPurposeStandard.NAICS_2017:
            return naics_2017()
        if self is BusinessPurposeStandard.SKD_2002:
            return skd_2002()
        if self is BusinessPurposeStandard.SKD_2008:
            return skd_2008()
        if self is BusinessPurposeStandard.TSIC_2552:
            return tsic_2552()
        if self is BusinessPurposeStandard.NACEBEL_2003:
            return nacebel_2003()
        if self is BusinessPurposeStandard.NACEBEL_2008:
            return nacebel_2008()
        if self is BusinessPurposeStandard.NAF_1:
            return naf_1()
        if self is BusinessPurposeStandard.NAF_2:
            return naf_2()
        if self is BusinessPurposeStandard.GCED_2011:
            return gced_2011()
        if self is BusinessPurposeStandard.SCIAN_2018:
            return scian_2018()
        if self is BusinessPurposeStandard.CCNAE_2021:
            return ccnae_2021()
        if self is BusinessPurposeStandard.CAEM_2005:
            return caem_2005()
        if self is BusinessPurposeStandard.SBI_2008:
            return sbi_2008()
        if self is BusinessPurposeStandard.HS:
            return hs()
        if self is BusinessPurposeStandard.SIC:
            return sic()
        if self is BusinessPurposeStandard.SSIC_2020:
            return ssic_2020()

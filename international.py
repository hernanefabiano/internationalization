#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

from collections import OrderedDict
import re

def get_country_name(country_code):
    '''
    Returns the localized name of a country given its ISO3166 country code
    '''
    if not isinstance(country_code, str):
        raise TypeError('country_code must be of type str')

    return _COUNTRY_CODE_TO_COUNTRY_NAME[country_code]


def get_native_country_name(country_code):
    '''
    Returns the localized name of a country given its ISO3166 country code
    '''
    if not isinstance(country_code, str):
        raise TypeError('country_code must be of type str')

    return _COUNTRY_CODE_TO_COUNTRY_NAME_NATIVE[country_code]


def get_region_name(region_id):
    '''
    Returns the localized name of a region given its region ID
    '''
    if not isinstance(region_id, str):
        raise TypeError('region_id must be of type str')

    return _REGION_ID_TO_REGION_NAME[region_id]


def get_international_sites():
    return _INTERNATIONAL_SITES

_INTERNATIONAL_SITES = [
    {'region_id': 'africa', 'country_code': 'za', 'url': 'https://countrycode.org/southafrica'},  
    {'region_id': 'europe', 'country_code': 'at', 'url': 'https://countrycode.org/austria'}, 
    {'region_id': 'europe', 'country_code': 'be', 'url': 'https://countrycode.org/belgium'}, 
    {'region_id': 'europe', 'country_code': 'fr', 'url': 'https://countrycode.org/france'}, 
    {'region_id': 'europe', 'country_code': 'de', 'url': 'https://countrycode.org/germany'}, 
    {'region_id': 'europe', 'country_code': 'nl', 'url': 'https://countrycode.org/netherlands'}, 
    {'region_id': 'asia-pacific', 'country_code': 'au', 'url': 'https://countrycode.org/australia'},      
    ]

_COUNTRY_CODE_TO_COUNTRY_NAME = {
    'za': 'South Africa',
    'at': 'Austria',
    'be': 'Belgium',
    'ch': 'Switzerland',
    'de': 'Germany',
    'es': 'Spain',
    'fr': 'France',
    'gb': 'United Kingdom',
    'ie': 'Ireland',
    'it': 'Italy',
    'nl': 'Netherlands',
    'pt': 'Portugal',
    'ru': 'Russia',
    'se': 'Sweden',
    'ar': 'Argentina',
    'br': 'Brazil',
    'ca': 'Canada',
    'mx': 'Mexico',
    'us': 'United States',
    'au': 'Australia',
    'in': 'India',
    'jp': 'Japan',
    'cn': 'China',
    'kr': 'Korea',
    }

_COUNTRY_CODE_TO_COUNTRY_NAME_NATIVE = {
    'za': u'South Africa',
    'at': u'Österreich',
    'be': u'België',
    'ch': u'Schweiz',
    'de': u'Deutschland',
    'es': u'España',
    'fr': u'France',
    'gb': u'United Kingdom',
    'ie': u'Ireland',
    'it': u'Italia',
    'nl': u'Nederland',
    'pt': u'Portugal',
    'ru': u'Россия',
    'se': u'Sverige',
    'ar': u'Argentina',
    'br': u'Brasil',
    'ca': u'Canada',
    'mx': u'México',
    'us': u'United States',
    'au': u'Australia',
    'in': u'India',
    'jp': u'日本',
    'cn': u'中国',
    'kr': u'한국',
    }

_REGION_ID_TO_REGION_NAME = {
    'africa': 'Africa',
    'americas': 'Americas',
    'asia-pacific': 'Asia/Pacific',
    'europe': 'Europe'
    }

def get_ordered_sites():
    '''Return an ordered dictionary of international sites, with just the main domain for url.'''
    url_regex = re.compile(r'^http://(?:www\.)?')
    international_sites = [
        (x['country_code'],
         {'url': re.sub(url_regex, '', x['url']),
          'native_name': get_native_country_name(x['country_code']),
          'name': get_country_name(x['country_code']),
          'country_code': x['country_code']
          }
         ) for x in _INTERNATIONAL_SITES
    ]
    international_sites = sorted(international_sites, key=lambda x: x[1]['name'])
    return OrderedDict(international_sites)

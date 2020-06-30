# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:56:24 2020

@author: The Absolute Tinkerer

All of the constants used throughout this program. Please note, some of the
"VAL_" keys are commented out - this is because that particular key has already
been instantiated elsewhere, and they both have the same value. I've left
these keys commented out as placeholders for user awareness that the key
already exists and is defined elsewhere.

The user should be extremely mindful not to redefine any existing keys, as it
may result in undesireable and unexpected issues. Plus troubleshooting would be
a pain.

To add new layers to render, you must create a CONFIG_STYLE key, VAL key, and
connect the VAL and CONFIG_STYLE in the DATA_GROUPS dictionary
"""

from PyQt5.QtCore import Qt


# Resource Strings
FOLDER_DATA = 'data'
FOLDER_OUTPUT = 'output'
FOLDER_CONFIGS = 'configs'
FOLDER_USER_CONFIGS = 'configs/user'
FILE_ICON = 'src/resources/icon.png'
FILE_CONFIG = 'user.config'


# Constants
DICT_QPEN_STYLE = {Qt.SolidLine:      'Solid Line',
                   Qt.DashLine:       'Dash Line',
                   Qt.DotLine:        'Dot Line',
                   Qt.DashDotLine:    'Dash-Dot Line',
                   Qt.DashDotDotLine: 'Dash-Dot-Dot Line'}
DICT_QPEN_CAP = {Qt.SquareCap:         'Square Cap',
                 Qt.FlatCap:           'Flat Cap',
                 Qt.RoundCap:          'Round Cap'}
DICT_QPEN_JOIN = {Qt.BevelJoin:         'Bevel Join',
                  Qt.MiterJoin:         'Miter Join',
                  Qt.RoundJoin:         'Round Join'}


# OSM File Features
COPYRIGHT = 'OpenStreetMap and contributors'
ATTRIBUTION = 'http://www.openstreetmap.org/copyright'
LICENSE = 'http://opendatacommons.org/licenses/odbl/1-0/'


# OSM tag keys
KEY_HIGHWAY = 'highway'
KEY_WATERWAY = 'waterway'
KEY_NATURAL = 'natural'
KEY_LANDUSE = 'landuse'
KEY_BUILDING = 'building'


# Configuration Keys - Styles
CONFIG_TYPE_QCOLOR = 'QColor'
CONFIG_TYPE_QPEN = 'QPen'

# The background color of the map
CONFIG_BG_COLOR = 'Background Color'

# KEY_HIGHWAY style keys
CONFIG_STYLE_MOTORWAY = 'Motorway Style'
CONFIG_STYLE_TRUNK = 'Trunk Style'
CONFIG_STYLE_PRIMARY = 'Primary Style'
CONFIG_STYLE_SECONDARY = 'Secondary Style'
CONFIG_STYLE_TERTIARY = 'Tertiary Style'
CONFIG_STYLE_UNCLASSIFIED = 'Unclassified Style'
CONFIG_STYLE_RESIDENTIAL = 'Residential Style'

CONFIG_STYLE_LINK_MOTORWAY = 'Motorway Link Style'
CONFIG_STYLE_LINK_TRUNK = 'Trunk Link Style'
CONFIG_STYLE_LINK_PRIMARY = 'Primary Link Style'
CONFIG_STYLE_LINK_SECONDARY = 'Secondary Link Style'
CONFIG_STYLE_LINK_TERTIARY = 'Tertiary Link Style'

CONFIG_STYLE_STREET = 'Street Style'
CONFIG_STYLE_SERVICE = 'Service Style'
CONFIG_STYLE_PEDESTRIAN = 'Pedestrian Style'
CONFIG_STYLE_TRACK = 'Track Style'
CONFIG_STYLE_BUS_GUIDEWAY = 'Bus Guideway Style'
CONFIG_STYLE_ESCAPE = 'Escape Style'
CONFIG_STYLE_RACEWAY = 'Raceway Style'
CONFIG_STYLE_ROAD = 'Road Style'
CONFIG_STYLE_FOOTWAY = 'Footway Style'
CONFIG_STYLE_BRIDLEWAY = 'Bridleway Style'
CONFIG_STYLE_STEPS = 'Steps Style'
CONFIG_STYLE_CORRIDOR = 'Corridor Style'
CONFIG_STYLE_PATH = 'Path Style'
CONFIG_STYLE_CYCLEWAY = 'Cycleway Style'
CONFIG_STYLE_PROPOSED = 'Proposed Style'
CONFIG_STYLE_CONSTRUCTION = 'Construction Style'

CONFIG_STYLE_BUS_STOP = 'Bus Stop Style'
CONFIG_STYLE_CROSSING = 'Crossing Style'
CONFIG_STYLE_ELEVATOR = 'Elevator Style'
CONFIG_STYLE_EMERG_POINT = 'Emergency Access Point Style'
CONFIG_STYLE_GIVE_WAY = 'Give Way Style'
CONFIG_STYLE_MILESTONE = 'Milestone Style'
CONFIG_STYLE_MINI_ROUNDABOUT = 'Mini Roundabout Style'
CONFIG_STYLE_MOTORWAY_JUNC = 'Motorway Junction Style'
CONFIG_STYLE_PASSING_PLACE = 'Passing Place Style'
CONFIG_STYLE_PLATFORM = 'Platform Style'
CONFIG_STYLE_REST_AREA = 'Rest Area Style'
CONFIG_STYLE_SPEED_CAMERA = 'Speed Camera Style'
CONFIG_STYLE_STREET_LAMP = 'Street Lamp Style'
CONFIG_STYLE_SERVICES = 'Services Style'
CONFIG_STYLE_STOP = 'Stop Style'
CONFIG_STYLE_TRAFFIC_MIRROR = 'Traffic Mirror Style'
CONFIG_STYLE_TRAFFIC_SIGNAL = 'Traffic Signals Style'
CONFIG_STYLE_TRAILHEAD = 'Trailhead Style'
CONFIG_STYLE_TURNING_CIRCLE = 'Turning Circle Style'
CONFIG_STYLE_TURNING_LOOP = 'Turning Loop Style'
CONFIG_STYLE_TOLL_GANTRY = 'Toll Gantry Style'

# KEY_NATURAL style keys
CONFIG_STYLE_RIVER = 'River Style'
CONFIG_STYLE_RIVERBANK = 'Riverbank Style'
CONFIG_STYLE_STREAM = 'Stream Style'
CONFIG_STYLE_TIDAL_CHANNEL = 'Tidal Channel Style'
CONFIG_STYLE_CANAL = 'Canal Style'
CONFIG_STYLE_PRESSURIZED = 'Pressurized Style'
CONFIG_STYLE_DRAIN = 'Drain Style'
CONFIG_STYLE_DITCH = 'Ditch Style'
CONFIG_STYLE_FAIRWAY = 'Fairway Style'
CONFIG_STYLE_ARTIFICIAL = 'Artificial Style'
CONFIG_STYLE_DERELICT = 'Derelict Canal Style'

CONFIG_STYLE_DOCK = 'Dock Style'
CONFIG_STYLE_BOATYARD = 'Boatyard Style'
CONFIG_STYLE_DAM = 'Dam Style'
CONFIG_STYLE_WEIR = 'Weir Style'
CONFIG_STYLE_FUEL = 'Fuel Style'
CONFIG_STYLE_LOCK_GATE = 'Lock Gate Style'

CONFIG_STYLE_WOOD = 'Wood Style'
CONFIG_STYLE_TREE_ROW = 'Tree Row Style'
CONFIG_STYLE_TREE = 'Tree Style'
CONFIG_STYLE_SCRUB = 'Scrub Style'
CONFIG_STYLE_HEATH = 'Heath Style'
CONFIG_STYLE_MOOR = 'Moor Style'
CONFIG_STYLE_GRASS = 'Grass Style'
CONFIG_STYLE_GRASSLAND = 'Grassland Style'
CONFIG_STYLE_FELL = 'Fell Style'
CONFIG_STYLE_BARE_ROCK = 'Bare Rock'
CONFIG_STYLE_SCREE = 'Scree Style'
CONFIG_STYLE_SHINGLE = 'Shingle Style'
CONFIG_STYLE_SAND = 'Sand Style'
CONFIG_STYLE_MUD = 'Mud Style'

CONFIG_STYLE_WATER = 'Water Style'
CONFIG_STYLE_WETLAND = 'Wetland'
CONFIG_STYLE_GLACIER = 'Glacier Style'
CONFIG_STYLE_BAY = 'Bay Style'
CONFIG_STYLE_CAPE = 'Cape Style'
CONFIG_STYLE_STRAIT = 'Strait Style'
CONFIG_STYLE_BEACH = 'Beach Style'
CONFIG_STYLE_COASTLINE = 'Coastline Style'
CONFIG_STYLE_REEF = 'Reef Style'
CONFIG_STYLE_SPRING = 'Spring Style'
CONFIG_STYLE_HOT_SPRING = 'Hot Spring Style'
CONFIG_STYLE_GEYSER = 'Geyser Style'
CONFIG_STYLE_MTN_RANGE = 'Mountain Range Style'

CONFIG_STYLE_PEAK = 'Peak Style'
CONFIG_STYLE_DUNE = 'Dune Style'
CONFIG_STYLE_HILL = 'Hill Style'
CONFIG_STYLE_VOLCANO = 'Volcano Style'
CONFIG_STYLE_VALLEY = 'Valley Style'
CONFIG_STYLE_RIDGE = 'Ridge Style'
CONFIG_STYLE_ARETE = 'Arete Style'
CONFIG_STYLE_CLIFF = 'Cliff Style'
CONFIG_STYLE_SADDLE = 'Saddle Style'
CONFIG_STYLE_ISTHMUS = 'Isthmus Style'
CONFIG_STYLE_PENINSULA = 'Peninsula Style'
CONFIG_STYLE_ROCK = 'Rock Style'
CONFIG_STYLE_STONE = 'Stone Style'
CONFIG_STYLE_SINKHOLE = 'Sinkhole Style'
CONFIG_STYLE_CAVE_ENTRANCE = 'Cave Entrance Style'

# KEY_LANDUSE style keys
CONFIG_STYLE_COMMERCIAL = 'Commercial Style'
CONFIG_STYLE_CONSTRUCTION_LU = 'Construction Land Use Style'
CONFIG_STYLE_INDUSTRIAL = 'Industrial Style'
CONFIG_STYLE_RESIDENTIAL_LU = 'Residential Land Use Style'
CONFIG_STYLE_RETAIL = 'Retail Style'
CONFIG_STYLE_ALLOTMENTS = 'Allotments Style'
CONFIG_STYLE_FARMLAND = 'Farmland Style'
CONFIG_STYLE_FARM = 'Farm Style'
CONFIG_STYLE_FARMYARD = 'Farmyard Style'
CONFIG_STYLE_FOREST = 'Forest Style'
CONFIG_STYLE_MEADOW = 'Meadow Style'
CONFIG_STYLE_ORCHARD = 'Orchard Style'
CONFIG_STYLE_VINEYARD = 'Vineyard Style'
CONFIG_STYLE_GARDEN = 'Garden Style'
CONFIG_STYLE_BASIN = 'Basin Style'
CONFIG_STYLE_BROWNFIELD = 'Brownfield Style'
CONFIG_STYLE_CEMETERY = 'Cemetery Style'
CONFIG_STYLE_CONSERVATION = 'Conservation Style'
CONFIG_STYLE_DEPOT = 'Depot Style'
CONFIG_STYLE_GARAGE = 'Garages Style'
CONFIG_STYLE_GARAGES = 'Garages Style'
CONFIG_STYLE_TRAF_ISLAND = 'Traffic Island Style'
CONFIG_STYLE_GRASS_LU = 'Grass Land Use Style'
CONFIG_STYLE_GREENFIELD = 'Greenfield Style'
CONFIG_STYLE_GH_HORT = 'Greenhouse Horticulture Style'
CONFIG_STYLE_LANDFILL = 'Landfill Style'
CONFIG_STYLE_MILITARY = 'Military Style'
CONFIG_STYLE_PEAT_CUTTING = 'Peat_cutting Style'
CONFIG_STYLE_PLANT_NURSERY = 'Plant Nursery Style'
CONFIG_STYLE_PORT = 'Port Style'
CONFIG_STYLE_QUARRY = 'Quarry Style'
CONFIG_STYLE_RAILWAY = 'Railway Style'
CONFIG_STYLE_REC_GROUND = 'Recreation Ground Style'
CONFIG_STYLE_RELIGIOUS = 'Religious Style'
CONFIG_STYLE_CHURCHYARD = 'Churchyard Style'
CONFIG_STYLE_RESERVOIR = 'Reservoir Style'
CONFIG_STYLE_RES_WTSHED = 'Reservoir Watershed Style'
CONFIG_STYLE_SALT_POND = 'Salt_pond Style'
CONFIG_STYLE_VILLAGE_GREEN = 'Village Green Style'
CONFIG_STYLE_VACANT = 'Vacant Style'
CONFIG_STYLE_YES_LU = 'Yes Land Use Style'
CONFIG_STYLE_GOVERNMENT_LU = 'Government Land Use Style'

# KEY_BUILDING style keys
CONFIG_STYLE_APARTMENTS = 'Apartments Style'
CONFIG_STYLE_INDOOR = 'Indoor Style'
CONFIG_STYLE_CONDOMINIUM = 'Condominium Style'
CONFIG_STYLE_CONDOMINIUM_2 = '(C)ondominium Style'
CONFIG_STYLE_TOWER = 'Tower Style'
CONFIG_STYLE_AMPHITHEATRE = 'Amphitheatre Style'
CONFIG_STYLE_BUNGALOW = 'Bungalow Style'
CONFIG_STYLE_CABIN = 'Cabin Style'
CONFIG_STYLE_DETACHED = 'Detached Style'
CONFIG_STYLE_DORMITORY = 'Dormitory Style'
CONFIG_STYLE_FARM_BLDG = 'Farm (Building) Style'
CONFIG_STYLE_GER = 'Ger Style'
CONFIG_STYLE_HOTEL = 'Hotel Style'
CONFIG_STYLE_HOUSE = 'House Style'
CONFIG_STYLE_HOUSEBOAT = 'Houseboat Style'
CONFIG_STYLE_RESID_BLDG = 'Residential (Building) Style'
CONFIG_STYLE_SD_HOUSE = 'Semidetached House Style'
CONFIG_STYLE_STATIC_CARAVAN = 'Static Caravan Style'
CONFIG_STYLE_TERRACE = 'Terrace Style'
CONFIG_STYLE_COMM_BLDG = 'Commercial (Building) Style'
CONFIG_STYLE_INDUSTRIAL_BLDG = 'Industrial (Building) Style'
CONFIG_STYLE_MANUFACTURE = 'Manufacture Style'
CONFIG_STYLE_KIOSK = 'Kiosk Style'
CONFIG_STYLE_OFFICE = 'Office Style'
CONFIG_STYLE_RETAIL_BLDG = 'Retail (Building) Style'
CONFIG_STYLE_SHOP = 'Shop Style'
CONFIG_STYLE_SUPERMARKET = 'Supermarket Style'
CONFIG_STYLE_WAREHOUSE = 'Warehouse Style'
CONFIG_STYLE_CATHEDRAL = 'Cathedral Style'
CONFIG_STYLE_CHAPEL = 'Chapel Style'
CONFIG_STYLE_CHURCH = 'Church Style'
CONFIG_STYLE_MOSQUE = 'Mosque Style'
CONFIG_STYLE_RELIGIOUS_BLDG = 'Religious (Building) Style'
CONFIG_STYLE_SHRINE = 'Shrine Style'
CONFIG_STYLE_SYNAGOGUE = 'Synagogue Style'
CONFIG_STYLE_TEMPLE = 'Temple Style'
CONFIG_STYLE_BAKEHOUSE = 'Bakehouse Style'
CONFIG_STYLE_CIVIC = 'Civic Style'
CONFIG_STYLE_GYM = 'Gym Style'
CONFIG_STYLE_CANOPY = 'Canopy Style'
CONFIG_STYLE_SHELTER = 'Shelter Style'
CONFIG_STYLE_BURIAL_VAULT = 'Burial Vault Style'
CONFIG_STYLE_PART = 'Part Style'
CONFIG_STYLE_COLLEGE = 'College Style'
CONFIG_STYLE_HEALTH = 'Health_Style'
CONFIG_STYLE_HOTEL_2 = '(H)otel Style'
CONFIG_STYLE_MULTIPURPOSE = 'Multipurpose Style'
CONFIG_STYLE_FIRE_STATION = 'Fire Station Style'
CONFIG_STYLE_GOVERNMENT = 'Government Style'
CONFIG_STYLE_GOVERNEMENT = 'Governement Style'  # An OSM misspelling...
CONFIG_STYLE_SUBWAY_ENTRY = 'Subway Entrance Style'
CONFIG_STYLE_LIBRARY = 'Library Style'
CONFIG_STYLE_HOSPITAL = 'Hospital Style'
CONFIG_STYLE_KINDERGARTEN = 'Kindergarten Style'
CONFIG_STYLE_PUBLIC = 'Public Style'
CONFIG_STYLE_SCHOOL = 'School Style'
CONFIG_STYLE_TOILETS = 'Toilets Style'
CONFIG_STYLE_TRAIN_STATION = 'Train Station Style'
CONFIG_STYLE_TRANSPORTATION = 'Transportation Style'
CONFIG_STYLE_UNIVERSITY = 'University Style'
CONFIG_STYLE_BARN = 'Barn Style'
CONFIG_STYLE_CONSERVATORY = 'Conservatory Style'
CONFIG_STYLE_COWSHED = 'Cowshed Style'
CONFIG_STYLE_FARM_AUXILIARY = 'Farm Auxiliary Style'
CONFIG_STYLE_GREENHOUSE = 'Greenhouse Style'
CONFIG_STYLE_SLURRY_TANK = 'Slurry Tank Style'
CONFIG_STYLE_STABLE = 'Stable Style'
CONFIG_STYLE_STY = 'Sty Style'
CONFIG_STYLE_GRANDSTAND = 'Grandstand Style'
CONFIG_STYLE_PAVILION = 'Pavilion Style'
CONFIG_STYLE_RIDING_HALL = 'Riding Hall Style'
CONFIG_STYLE_SPORTS_HALL = 'Sports_ Hall Style'
CONFIG_STYLE_STADIUM = 'Stadium Style'
CONFIG_STYLE_HANGAR = 'Hangar Style'
CONFIG_STYLE_HUT = 'Hut Style'
CONFIG_STYLE_SHED = 'Shed Style'
CONFIG_STYLE_CARPORT = 'Carport Style'
CONFIG_STYLE_GARAGE_BLDG = 'Garage Style'
CONFIG_STYLE_GARAGES_BLDG = 'Garages (Building) Style'
CONFIG_STYLE_PARKING = 'Parking Style'
CONFIG_STYLE_DIGESTER = 'Digester Style'
CONFIG_STYLE_SERVICE_BLDG = 'Service (Building) Style'
CONFIG_STYLE_TRANSF_TOWER = 'Transformer Tower Style'
CONFIG_STYLE_WATER_TOWER = 'Water Tower Style'
CONFIG_STYLE_BUNKER = 'Bunker Style'
CONFIG_STYLE_BRIDGE = 'Bridge Style'
CONFIG_STYLE_CONSTR_BLDG = 'Construction (Building) Style'
CONFIG_STYLE_GATEHOUSE = 'Gatehouse Style'
CONFIG_STYLE_ROOF = 'Roof Style'
CONFIG_STYLE_RUINS = 'Ruins Style'
CONFIG_STYLE_TREE_HOUSE = 'Tree House Style'
CONFIG_STYLE_YES = 'Yes Style'
CONFIG_STYLE_NO = 'No Style'
CONFIG_STYLE_UNDEF = 'Undefined Style'


# OSM tag KEY_HIGHWAY values
# see: https://wiki.openstreetmap.org/wiki/Key:highway
VAL_MOTORWAY = 'motorway'
VAL_TRUNK = 'trunk'
VAL_PRIMARY = 'primary'
VAL_SECONDARY = 'secondary'
VAL_TERTIARY = 'tertiary'
VAL_UNCLASSIFIED = 'unclassified'
VAL_RESIDENTIAL = 'residential'

VAL_LINK_MOTORWAY = 'motorway_link'
VAL_LINK_TRUNK = 'trunk_link'
VAL_LINK_PRIMARY = 'primary_link'
VAL_LINK_SECONDARY = 'secondary_link'
VAL_LINK_TERTIARY = 'tertiary_link'

VAL_STREET = 'living_street'
VAL_SERVICE = 'service'
VAL_PEDESTRIAN = 'pedestrian'
VAL_TRACK = 'track'
VAL_BUS_GUIDEWAY = 'bus_guideway'
VAL_ESCAPE = 'escape'
VAL_RACEWAY = 'raceway'
VAL_ROAD = 'road'
VAL_FOOTWAY = 'footway'
VAL_BRIDLEWAY = 'bridleway'
VAL_STEPS = 'steps'
VAL_CORRIDOR = 'corridor'
VAL_PATH = 'path'
VAL_CYCLEWAY = 'cycleway'
VAL_PROPOSED = 'proposed'
VAL_CONSTRUCTION = 'construction'

VAL_BUS_STOP = 'bus_stop'
VAL_CROSSING = 'crossing'
VAL_ELEVATOR = 'elevator'
VAL_EMERG_POINT = 'emergency_access_point'
VAL_GIVE_WAY = 'give_way'
VAL_MILESTONE = 'milestone'
VAL_MINI_RABOUT = 'mini_roundabout'
VAL_MOTORWAY_JUNC = 'motorway_junction'
VAL_PASSING_PLACE = 'passing_place'
VAL_PLATFORM = 'platform'
VAL_REST_AREA = 'rest_area'
VAL_SPEED_CAMERA = 'speed_camera'
VAL_STREET_LAMP = 'street_lamp'
VAL_SERVICES = 'services'
VAL_STOP = 'stop'
VAL_TRAFFIC_MIRROR = 'traffic_mirror'
VAL_TRAFFIC_SIGNAL = 'traffic_signals'
VAL_TRAILHEAD = 'trailhead'
VAL_TURNING_CIRCLE = 'turning_circle'
VAL_TURNING_LOOP = 'turning_loop'
VAL_TOLL_GANTRY = 'toll_gantry'


# OSM tag KEY_WATERWAY values
VAL_RIVER = 'river'
VAL_RIVERBANK = 'riverbank'
VAL_STREAM = 'stream'
VAL_TIDAL_CHANNEL = 'tidal_channel'
VAL_CANAL = 'canal'
VAL_PRESSURIZED = 'pressurised'
VAL_DRAIN = 'drain'
VAL_DITCH = 'ditch'
VAL_FAIRWAY = 'fairway'
VAL_ARTIFICIAL = 'artificial'
VAL_DERELICT = 'derelict_canal'

VAL_DOCK = 'dock'
VAL_BOATYARD = 'boatyard'
VAL_DAM = 'dam'
VAL_WEIR = 'weir'
VAL_FUEL = 'fuel'
VAL_LOCK_GATE = 'lock_gate'


# OSM tag KEY_NATURAL values
VAL_WOOD = 'wood'
VAL_TREE_ROW = 'tree_row'
VAL_TREE = 'tree'
VAL_SCRUB = 'scrub'
VAL_HEATH = 'heath'
VAL_MOOR = 'moor'
VAL_GRASS = 'grass'
VAL_GRASSLAND = 'grassland'
VAL_FELL = 'fell'
VAL_BARE_ROCK = 'bare_rock'
VAL_SCREE = 'scree'
VAL_SHINGLE = 'shingle'
VAL_SAND = 'sand'
VAL_MUD = 'mud'

VAL_WATER = 'water'
VAL_WETLAND = 'wetland'
VAL_GLACIER = 'glacier'
VAL_BAY = 'bay'
VAL_CAPE = 'cape'
VAL_STRAIT = 'strait'
VAL_BEACH = 'beach'
VAL_COASTLINE = 'coastline'
VAL_REEF = 'reef'
VAL_SPRING = 'spring'
VAL_HOT_SPRING = 'hot_spring'
VAL_GEYSER = 'geyser'
VAL_MTN_RANGE = 'mountain_range'

VAL_PEAK = 'peak'
VAL_DUNE = 'dune'
VAL_HILL = 'hill'
VAL_VOLCANO = 'volcano'
VAL_VALLEY = 'valley'
VAL_RIDGE = 'ridge'
VAL_ARETE = 'arete'
VAL_CLIFF = 'cliff'
VAL_SADDLE = 'saddle'
VAL_ISTHMUS = 'isthmus'
VAL_PENINSULA = 'peninsula'
VAL_ROCK = 'rock'
VAL_STONE = 'stone'
VAL_SINKHOLE = 'sinkhole'
VAL_CAVE_ENTRANCE = 'cave_entrance'


# OSM tag KEY_LANDUSE values
VAL_COMMERCIAL = 'commercial'
# VAL_CONSTRUCTION = 'construction'
VAL_INDUSTRIAL = 'industrial'
# VAL_RESIDENTIAL = 'residential'
VAL_RETAIL = 'retail'
VAL_ALLOTMENTS = 'allotments'
VAL_FARMLAND = 'farmland'
VAL_FARM = 'farm'
VAL_FARMYARD = 'farmyard'
VAL_FOREST = 'forest'
VAL_MEADOW = 'meadow'
VAL_ORCHARD = 'orchard'
VAL_VINEYARD = 'vineyard'
VAL_GARDEN = 'Garden'
VAL_BASIN = 'basin'
VAL_BROWNFIELD = 'brownfield'
VAL_CEMETERY = 'cemetery'
VAL_CONSERVATION = 'conservation'
VAL_DEPOT = 'depot'
VAL_GARAGE = 'garage'
VAL_GARAGES = 'garages'
VAL_TRAF_ISLAND = 'traffic_island'
# VAL_GRASS = 'grass'
VAL_GREENFIELD = 'greenfield'
VAL_GH_HORT = 'greenhouse_horticulture'
VAL_LANDFILL = 'landfill'
VAL_MILITARY = 'military'
VAL_PEAT_CUTTING = 'peat_cutting'
VAL_PLANT_NURSERY = 'plant_nursery'
VAL_PORT = 'port'
VAL_QUARRY = 'quarry'
VAL_RAILWAY = 'railway'
VAL_REC_GROUND = 'recreation_ground'
VAL_RELIGIOUS = 'religious'
VAL_CHURCHYARD = 'churchyard'
VAL_RESERVOIR = 'reservoir'
VAL_RES_WTSHED = 'reservoir_watershed'
VAL_SALT_POND = 'salt_pond'
VAL_VILLAGE_GREEN = 'village_green'
VAL_VACANT = 'vacant'
VAL_YES_LU = 'yes'
VAL_GOVERNMENT_LU = 'government'


# OSM tag KEY_BUILDING values
VAL_APARTMENTS = 'apartments'
VAL_INDOOR = 'indoor'
VAL_CONDOMINIUM = 'condominium'
VAL_CONDOMINIUM_2 = 'Condominium'
VAL_TOWER = 'tower'
VAL_AMPHITHEATRE = 'amphitheatre'
VAL_BUNGALOW = 'bungalow'
VAL_CABIN = 'cabin'
VAL_DETACHED = 'detached'
VAL_DORMITORY = 'dormitory'
# VAL_FARM = 'farm'
VAL_GER = 'ger'
VAL_HOTEL = 'hotel'
VAL_HOUSE = 'house'
VAL_HOUSEBOAT = 'houseboat'
# VAL_RESIDENTIAL = 'residential'
VAL_SD_HOUSE = 'semidetached_house'
VAL_STATIC_CARAVAN = 'static_caravan'
VAL_TERRACE = 'terrace'
# VAL_COMMERCIAL = 'commercial'
# VAL_INDUSTRIAL = 'industrial'
VAL_MANUFACTURE = 'manufacture'
VAL_KIOSK = 'kiosk'
VAL_OFFICE = 'office'
# VAL_RETAIL = 'retail'
VAL_SHOP = 'shop'
VAL_SUPERMARKET = 'supermarket'
VAL_WAREHOUSE = 'warehouse'
VAL_CATHEDRAL = 'cathedral'
VAL_CHAPEL = 'chapel'
VAL_CHURCH = 'church'
VAL_MOSQUE = 'mosque'
# VAL_RELIGIOUS = 'religious'
VAL_SHRINE = 'shrine'
VAL_SYNAGOGUE = 'synagogue'
VAL_TEMPLE = 'temple'
VAL_BAKEHOUSE = 'bakehouse'
VAL_CIVIC = 'civic'
VAL_GYM = 'Gym'
VAL_CANOPY = 'canopy'
VAL_SHELTER = 'shelter'
VAL_BURIAL_VAULT = 'burial_vault'
VAL_PART = 'part'
VAL_COLLEGE = 'college'
VAL_HEALTH = 'health'
VAL_HOTEL_2 = 'Hotel'
VAL_MULTIPURPOSE = 'multipurpose'
VAL_FIRE_STATION = 'fire_station'
VAL_GOVERNMENT = 'government'
VAL_GOVERNEMENT = 'governement'  # This was a misspelling in some OSM files...
VAL_SUBWAY_ENTRY = 'subway_entrance'
VAL_LIBRARY = 'library'
VAL_HOSPITAL = 'hospital'
VAL_KINDERGARTEN = 'kindergarten'
VAL_PUBLIC = 'public'
VAL_SCHOOL = 'school'
VAL_TOILETS = 'toilets'
VAL_TRAIN_STATION = 'train_station'
VAL_TRANSPORTATION = 'transportation'
VAL_UNIVERSITY = 'university'
VAL_BARN = 'barn'
VAL_CONSERVATORY = 'conservatory'
VAL_COWSHED = 'cowshed'
VAL_FARM_AUXILIARY = 'farm_auxiliary'
VAL_GREENHOUSE = 'greenhouse'
VAL_SLURRY_TANK = 'slurry_tank'
VAL_STABLE = 'stable'
VAL_STY = 'sty'
VAL_GRANDSTAND = 'grandstand'
VAL_PAVILION = 'pavilion'
VAL_RIDING_HALL = 'riding_hall'
VAL_SPORTS_HALL = 'sports_hall'
VAL_STADIUM = 'stadium'
VAL_HANGAR = 'hangar'
VAL_HUT = 'hut'
VAL_SHED = 'shed'
VAL_CARPORT = 'carport'
# VAL_GARAGE = 'garage'
# VAL_GARAGES = 'garages'
VAL_PARKING = 'parking'
VAL_DIGESTER = 'digester'
# VAL_SERVICE = 'service'
VAL_TRANSF_TOWER = 'transformer_tower'
VAL_WATER_TOWER = 'water_tower'
VAL_BUNKER = 'bunker'
VAL_BRIDGE = 'bridge'
# VAL_CONSTRUCTION = 'construction'
VAL_GATEHOUSE = 'gatehouse'
VAL_ROOF = 'roof'
VAL_RUINS = 'ruins'
VAL_TREE_HOUSE = 'tree_house'
VAL_YES = 'yes'
VAL_NO = 'no'
VAL_UNDEF = 'undefined'

# Connect the OSM groups to the proper setting
DATA_GROUPS = {KEY_HIGHWAY:  {VAL_MOTORWAY:       CONFIG_STYLE_MOTORWAY,
                              VAL_TRUNK:          CONFIG_STYLE_TRUNK,
                              VAL_PRIMARY:        CONFIG_STYLE_PRIMARY,
                              VAL_SECONDARY:      CONFIG_STYLE_SECONDARY,
                              VAL_TERTIARY:       CONFIG_STYLE_TERTIARY,
                              VAL_UNCLASSIFIED:   CONFIG_STYLE_UNCLASSIFIED,
                              VAL_RESIDENTIAL:    CONFIG_STYLE_RESIDENTIAL,
                              VAL_LINK_MOTORWAY:  CONFIG_STYLE_LINK_MOTORWAY,
                              VAL_LINK_TRUNK:     CONFIG_STYLE_LINK_TRUNK,
                              VAL_LINK_PRIMARY:   CONFIG_STYLE_LINK_PRIMARY,
                              VAL_LINK_SECONDARY: CONFIG_STYLE_LINK_SECONDARY,
                              VAL_LINK_TERTIARY:  CONFIG_STYLE_LINK_TERTIARY,
                              VAL_STREET:         CONFIG_STYLE_STREET,
                              VAL_SERVICE:        CONFIG_STYLE_SERVICE,
                              VAL_PEDESTRIAN:     CONFIG_STYLE_PEDESTRIAN,
                              VAL_TRACK:          CONFIG_STYLE_TRACK,
                              VAL_BUS_GUIDEWAY:   CONFIG_STYLE_BUS_GUIDEWAY,
                              VAL_ESCAPE:         CONFIG_STYLE_ESCAPE,
                              VAL_RACEWAY:        CONFIG_STYLE_RACEWAY,
                              VAL_ROAD:           CONFIG_STYLE_ROAD,
                              VAL_FOOTWAY:        CONFIG_STYLE_FOOTWAY,
                              VAL_BRIDLEWAY:      CONFIG_STYLE_BRIDLEWAY,
                              VAL_STEPS:          CONFIG_STYLE_STEPS,
                              VAL_CORRIDOR:       CONFIG_STYLE_CORRIDOR,
                              VAL_PATH:           CONFIG_STYLE_PATH,
                              VAL_CYCLEWAY:       CONFIG_STYLE_CYCLEWAY,
                              VAL_PROPOSED:       CONFIG_STYLE_PROPOSED,
                              VAL_CONSTRUCTION:   CONFIG_STYLE_CONSTRUCTION,
                              VAL_BUS_STOP:       CONFIG_STYLE_BUS_STOP,
                              VAL_CROSSING:       CONFIG_STYLE_CROSSING,
                              VAL_ELEVATOR:       CONFIG_STYLE_ELEVATOR,
                              VAL_EMERG_POINT:    CONFIG_STYLE_EMERG_POINT,
                              VAL_GIVE_WAY:       CONFIG_STYLE_GIVE_WAY,
                              VAL_MILESTONE:      CONFIG_STYLE_MILESTONE,
                              VAL_MINI_RABOUT:    CONFIG_STYLE_MINI_ROUNDABOUT,
                              VAL_MOTORWAY_JUNC:  CONFIG_STYLE_MOTORWAY_JUNC,
                              VAL_PASSING_PLACE:  CONFIG_STYLE_PASSING_PLACE,
                              VAL_PLATFORM:       CONFIG_STYLE_PLATFORM,
                              VAL_REST_AREA:      CONFIG_STYLE_REST_AREA,
                              VAL_SPEED_CAMERA:   CONFIG_STYLE_SPEED_CAMERA,
                              VAL_STREET_LAMP:    CONFIG_STYLE_STREET_LAMP,
                              VAL_SERVICES:       CONFIG_STYLE_SERVICES,
                              VAL_STOP:           CONFIG_STYLE_STOP,
                              VAL_TRAFFIC_MIRROR: CONFIG_STYLE_TRAFFIC_MIRROR,
                              VAL_TRAFFIC_SIGNAL: CONFIG_STYLE_TRAFFIC_SIGNAL,
                              VAL_TRAILHEAD:      CONFIG_STYLE_TRAILHEAD,
                              VAL_TURNING_CIRCLE: CONFIG_STYLE_TURNING_CIRCLE,
                              VAL_TURNING_LOOP:   CONFIG_STYLE_TURNING_LOOP,
                              VAL_TOLL_GANTRY:    CONFIG_STYLE_TOLL_GANTRY},
               KEY_WATERWAY: {VAL_RIVER:          CONFIG_STYLE_RIVER,
                              VAL_RIVERBANK:      CONFIG_STYLE_RIVERBANK,
                              VAL_STREAM:         CONFIG_STYLE_STREAM,
                              VAL_TIDAL_CHANNEL:  CONFIG_STYLE_TIDAL_CHANNEL,
                              VAL_CANAL:          CONFIG_STYLE_CANAL,
                              VAL_PRESSURIZED:    CONFIG_STYLE_PRESSURIZED,
                              VAL_DRAIN:          CONFIG_STYLE_DRAIN,
                              VAL_DITCH:          CONFIG_STYLE_DITCH,
                              VAL_FAIRWAY:        CONFIG_STYLE_FAIRWAY,
                              VAL_ARTIFICIAL:     CONFIG_STYLE_ARTIFICIAL,
                              VAL_DERELICT:       CONFIG_STYLE_DERELICT,
                              VAL_DOCK:           CONFIG_STYLE_DOCK,
                              VAL_BOATYARD:       CONFIG_STYLE_BOATYARD,
                              VAL_DAM:            CONFIG_STYLE_DAM,
                              VAL_WEIR:           CONFIG_STYLE_WEIR,
                              VAL_FUEL:           CONFIG_STYLE_FUEL,
                              VAL_LOCK_GATE:      CONFIG_STYLE_LOCK_GATE},
               KEY_NATURAL:  {VAL_WOOD:           CONFIG_STYLE_WOOD,
                              VAL_TREE_ROW:       CONFIG_STYLE_TREE_ROW,
                              VAL_TREE:           CONFIG_STYLE_TREE,
                              VAL_SCRUB:          CONFIG_STYLE_SCRUB,
                              VAL_HEATH:          CONFIG_STYLE_HEATH,
                              VAL_MOOR:           CONFIG_STYLE_MOOR,
                              VAL_GRASS:          CONFIG_STYLE_GRASS,
                              VAL_GRASSLAND:      CONFIG_STYLE_GRASSLAND,
                              VAL_FELL:           CONFIG_STYLE_FELL,
                              VAL_BARE_ROCK:      CONFIG_STYLE_BARE_ROCK,
                              VAL_SCREE:          CONFIG_STYLE_SCREE,
                              VAL_SHINGLE:        CONFIG_STYLE_SHINGLE,
                              VAL_SAND:           CONFIG_STYLE_SAND,
                              VAL_MUD:            CONFIG_STYLE_MUD,
                              VAL_WATER:          CONFIG_STYLE_WATER,
                              VAL_WETLAND:        CONFIG_STYLE_WETLAND,
                              VAL_GLACIER:        CONFIG_STYLE_GLACIER,
                              VAL_BAY:            CONFIG_STYLE_BAY,
                              VAL_CAPE:           CONFIG_STYLE_CAPE,
                              VAL_STRAIT:         CONFIG_STYLE_STRAIT,
                              VAL_BEACH:          CONFIG_STYLE_BEACH,
                              VAL_COASTLINE:      CONFIG_STYLE_COASTLINE,
                              VAL_REEF:           CONFIG_STYLE_REEF,
                              VAL_SPRING:         CONFIG_STYLE_SPRING,
                              VAL_HOT_SPRING:     CONFIG_STYLE_HOT_SPRING,
                              VAL_GEYSER:         CONFIG_STYLE_GEYSER,
                              VAL_MTN_RANGE:      CONFIG_STYLE_MTN_RANGE,
                              VAL_PEAK:           CONFIG_STYLE_PEAK,
                              VAL_DUNE:           CONFIG_STYLE_DUNE,
                              VAL_HILL:           CONFIG_STYLE_HILL,
                              VAL_VOLCANO:        CONFIG_STYLE_VOLCANO,
                              VAL_VALLEY:         CONFIG_STYLE_VALLEY,
                              VAL_RIDGE:          CONFIG_STYLE_RIDGE,
                              VAL_ARETE:          CONFIG_STYLE_ARETE,
                              VAL_CLIFF:          CONFIG_STYLE_CLIFF,
                              VAL_SADDLE:         CONFIG_STYLE_SADDLE,
                              VAL_ISTHMUS:        CONFIG_STYLE_ISTHMUS,
                              VAL_PENINSULA:      CONFIG_STYLE_PENINSULA,
                              VAL_ROCK:           CONFIG_STYLE_ROCK,
                              VAL_STONE:          CONFIG_STYLE_STONE,
                              VAL_SINKHOLE:       CONFIG_STYLE_SINKHOLE,
                              VAL_CAVE_ENTRANCE:  CONFIG_STYLE_CAVE_ENTRANCE},
               KEY_LANDUSE:  {VAL_COMMERCIAL:     CONFIG_STYLE_COMMERCIAL,
                              VAL_CONSTRUCTION:   CONFIG_STYLE_CONSTRUCTION_LU,
                              VAL_INDUSTRIAL:     CONFIG_STYLE_INDUSTRIAL,
                              VAL_RESIDENTIAL:    CONFIG_STYLE_RESIDENTIAL_LU,
                              VAL_RETAIL:         CONFIG_STYLE_RETAIL,
                              VAL_ALLOTMENTS:     CONFIG_STYLE_ALLOTMENTS,
                              VAL_FARMLAND:       CONFIG_STYLE_FARMLAND,
                              VAL_FARM:           CONFIG_STYLE_FARM,
                              VAL_FARMYARD:       CONFIG_STYLE_FARMYARD,
                              VAL_FOREST:         CONFIG_STYLE_FOREST,
                              VAL_MEADOW:         CONFIG_STYLE_MEADOW,
                              VAL_ORCHARD:        CONFIG_STYLE_ORCHARD,
                              VAL_VINEYARD:       CONFIG_STYLE_VINEYARD,
                              VAL_GARDEN:         CONFIG_STYLE_GARDEN,
                              VAL_BASIN:          CONFIG_STYLE_BASIN,
                              VAL_BROWNFIELD:     CONFIG_STYLE_BROWNFIELD,
                              VAL_CEMETERY:       CONFIG_STYLE_CEMETERY,
                              VAL_CONSERVATION:   CONFIG_STYLE_CONSERVATION,
                              VAL_DEPOT:          CONFIG_STYLE_DEPOT,
                              VAL_GARAGE:         CONFIG_STYLE_GARAGE,
                              VAL_GARAGES:        CONFIG_STYLE_GARAGES,
                              VAL_TRAF_ISLAND:    CONFIG_STYLE_TRAF_ISLAND,
                              VAL_GRASS:          CONFIG_STYLE_GRASS_LU,
                              VAL_GREENFIELD:     CONFIG_STYLE_GREENFIELD,
                              VAL_GH_HORT:        CONFIG_STYLE_GH_HORT,
                              VAL_LANDFILL:       CONFIG_STYLE_LANDFILL,
                              VAL_MILITARY:       CONFIG_STYLE_MILITARY,
                              VAL_PEAT_CUTTING:   CONFIG_STYLE_PEAT_CUTTING,
                              VAL_PLANT_NURSERY:  CONFIG_STYLE_PLANT_NURSERY,
                              VAL_PORT:           CONFIG_STYLE_PORT,
                              VAL_QUARRY:         CONFIG_STYLE_QUARRY,
                              VAL_RAILWAY:        CONFIG_STYLE_RAILWAY,
                              VAL_REC_GROUND:     CONFIG_STYLE_REC_GROUND,
                              VAL_RELIGIOUS:      CONFIG_STYLE_RELIGIOUS,
                              VAL_CHURCHYARD:     CONFIG_STYLE_CHURCHYARD,
                              VAL_RESERVOIR:      CONFIG_STYLE_RESERVOIR,
                              VAL_RES_WTSHED:     CONFIG_STYLE_RES_WTSHED,
                              VAL_SALT_POND:      CONFIG_STYLE_SALT_POND,
                              VAL_VILLAGE_GREEN:  CONFIG_STYLE_VILLAGE_GREEN,
                              VAL_VACANT:         CONFIG_STYLE_VACANT,
                              VAL_YES_LU:         CONFIG_STYLE_YES_LU,
                              VAL_GOVERNMENT_LU:  CONFIG_STYLE_GOVERNMENT_LU},
               KEY_BUILDING: {VAL_APARTMENTS:     CONFIG_STYLE_APARTMENTS,
                              VAL_INDOOR:         CONFIG_STYLE_INDOOR,
                              VAL_CONDOMINIUM:    CONFIG_STYLE_CONDOMINIUM,
                              VAL_CONDOMINIUM_2:  CONFIG_STYLE_CONDOMINIUM_2,
                              VAL_TOWER:          CONFIG_STYLE_TOWER,
                              VAL_AMPHITHEATRE:   CONFIG_STYLE_AMPHITHEATRE,
                              VAL_BUNGALOW:       CONFIG_STYLE_BUNGALOW,
                              VAL_CABIN:          CONFIG_STYLE_CABIN,
                              VAL_DETACHED:       CONFIG_STYLE_DETACHED,
                              VAL_DORMITORY:      CONFIG_STYLE_DORMITORY,
                              VAL_FARM:           CONFIG_STYLE_FARM_BLDG,
                              VAL_GER:            CONFIG_STYLE_GER,
                              VAL_HOTEL:          CONFIG_STYLE_HOTEL,
                              VAL_HOUSE:          CONFIG_STYLE_HOUSE,
                              VAL_HOUSEBOAT:      CONFIG_STYLE_HOUSEBOAT,
                              VAL_RESIDENTIAL:    CONFIG_STYLE_RESID_BLDG,
                              VAL_SD_HOUSE:       CONFIG_STYLE_SD_HOUSE,
                              VAL_STATIC_CARAVAN: CONFIG_STYLE_STATIC_CARAVAN,
                              VAL_TERRACE:        CONFIG_STYLE_TERRACE,
                              VAL_COMMERCIAL:     CONFIG_STYLE_COMM_BLDG,
                              VAL_INDUSTRIAL:     CONFIG_STYLE_INDUSTRIAL_BLDG,
                              VAL_MANUFACTURE:    CONFIG_STYLE_MANUFACTURE,
                              VAL_KIOSK:          CONFIG_STYLE_KIOSK,
                              VAL_OFFICE:         CONFIG_STYLE_OFFICE,
                              VAL_RETAIL:         CONFIG_STYLE_RETAIL_BLDG,
                              VAL_SHOP:           CONFIG_STYLE_SHOP,
                              VAL_SUPERMARKET:    CONFIG_STYLE_SUPERMARKET,
                              VAL_WAREHOUSE:      CONFIG_STYLE_WAREHOUSE,
                              VAL_CATHEDRAL:      CONFIG_STYLE_CATHEDRAL,
                              VAL_CHAPEL:         CONFIG_STYLE_CHAPEL,
                              VAL_CHURCH:         CONFIG_STYLE_CHURCH,
                              VAL_MOSQUE:         CONFIG_STYLE_MOSQUE,
                              VAL_RELIGIOUS:      CONFIG_STYLE_RELIGIOUS_BLDG,
                              VAL_SHRINE:         CONFIG_STYLE_SHRINE,
                              VAL_SYNAGOGUE:      CONFIG_STYLE_SYNAGOGUE,
                              VAL_TEMPLE:         CONFIG_STYLE_TEMPLE,
                              VAL_BAKEHOUSE:      CONFIG_STYLE_BAKEHOUSE,
                              VAL_CIVIC:          CONFIG_STYLE_CIVIC,
                              VAL_GYM:            CONFIG_STYLE_GYM,
                              VAL_CANOPY:         CONFIG_STYLE_CANOPY,
                              VAL_SHELTER:        CONFIG_STYLE_SHELTER,
                              VAL_BURIAL_VAULT:   CONFIG_STYLE_BURIAL_VAULT,
                              VAL_PART:           CONFIG_STYLE_PART,
                              VAL_COLLEGE:        CONFIG_STYLE_COLLEGE,
                              VAL_HEALTH:         CONFIG_STYLE_HEALTH,
                              VAL_HOTEL_2:        CONFIG_STYLE_HOTEL_2,
                              VAL_MULTIPURPOSE:   CONFIG_STYLE_MULTIPURPOSE,
                              VAL_FIRE_STATION:   CONFIG_STYLE_FIRE_STATION,
                              VAL_GOVERNMENT:     CONFIG_STYLE_GOVERNMENT,
                              VAL_GOVERNEMENT:    CONFIG_STYLE_GOVERNEMENT,
                              VAL_SUBWAY_ENTRY:   CONFIG_STYLE_SUBWAY_ENTRY,
                              VAL_LIBRARY:        CONFIG_STYLE_LIBRARY,
                              VAL_HOSPITAL:       CONFIG_STYLE_HOSPITAL,
                              VAL_KINDERGARTEN:   CONFIG_STYLE_KINDERGARTEN,
                              VAL_PUBLIC:         CONFIG_STYLE_PUBLIC,
                              VAL_SCHOOL:         CONFIG_STYLE_SCHOOL,
                              VAL_TOILETS:        CONFIG_STYLE_TOILETS,
                              VAL_TRAIN_STATION:  CONFIG_STYLE_TRAIN_STATION,
                              VAL_TRANSPORTATION: CONFIG_STYLE_TRANSPORTATION,
                              VAL_UNIVERSITY:     CONFIG_STYLE_UNIVERSITY,
                              VAL_BARN:           CONFIG_STYLE_BARN,
                              VAL_CONSERVATORY:   CONFIG_STYLE_CONSERVATORY,
                              VAL_COWSHED:        CONFIG_STYLE_COWSHED,
                              VAL_FARM_AUXILIARY: CONFIG_STYLE_FARM_AUXILIARY,
                              VAL_GREENHOUSE:     CONFIG_STYLE_GREENHOUSE,
                              VAL_SLURRY_TANK:    CONFIG_STYLE_SLURRY_TANK,
                              VAL_STABLE:         CONFIG_STYLE_STABLE,
                              VAL_STY:            CONFIG_STYLE_STY,
                              VAL_GRANDSTAND:     CONFIG_STYLE_GRANDSTAND,
                              VAL_PAVILION:       CONFIG_STYLE_PAVILION,
                              VAL_RIDING_HALL:    CONFIG_STYLE_RIDING_HALL,
                              VAL_SPORTS_HALL:    CONFIG_STYLE_SPORTS_HALL,
                              VAL_STADIUM:        CONFIG_STYLE_STADIUM,
                              VAL_HANGAR:         CONFIG_STYLE_HANGAR,
                              VAL_HUT:            CONFIG_STYLE_HUT,
                              VAL_SHED:           CONFIG_STYLE_SHED,
                              VAL_CARPORT:        CONFIG_STYLE_CARPORT,
                              VAL_GARAGE:         CONFIG_STYLE_GARAGE_BLDG,
                              VAL_GARAGES:        CONFIG_STYLE_GARAGES_BLDG,
                              VAL_PARKING:        CONFIG_STYLE_PARKING,
                              VAL_DIGESTER:       CONFIG_STYLE_DIGESTER,
                              VAL_SERVICE:        CONFIG_STYLE_SERVICE_BLDG,
                              VAL_TRANSF_TOWER:   CONFIG_STYLE_TRANSF_TOWER,
                              VAL_WATER_TOWER:    CONFIG_STYLE_WATER_TOWER,
                              VAL_BUNKER:         CONFIG_STYLE_BUNKER,
                              VAL_BRIDGE:         CONFIG_STYLE_BRIDGE,
                              VAL_CONSTRUCTION:   CONFIG_STYLE_CONSTR_BLDG,
                              VAL_GATEHOUSE:      CONFIG_STYLE_GATEHOUSE,
                              VAL_ROOF:           CONFIG_STYLE_ROOF,
                              VAL_RUINS:          CONFIG_STYLE_RUINS,
                              VAL_TREE_HOUSE:     CONFIG_STYLE_TREE_HOUSE,
                              VAL_YES:            CONFIG_STYLE_YES,
                              VAL_NO:             CONFIG_STYLE_NO,
                              VAL_UNDEF:          CONFIG_STYLE_UNDEF}}


# specifying columns for imputation
impute_col_most_freq = ['County','City']
categorical_col_encoding = ['County','City','Make','Model','Electric Vehicle Type','Clean Alternative Fuel Vehicle (CAFV) Eligibility']# try ,'Model Year' later
numerical_col_normalize = ['DOL Vehicle ID', '2020 Census Tract']
x_drop = ['Electric Range']








county = ['King', 'Yakima', 'Thurston', 'Snohomish', 'Island', 'Kitsap',
              'Whatcom', 'Pierce', 'Whitman', 'Skagit', 'Kittitas', 'Spokane',
              'Walla Walla', 'Chelan', 'Grant', 'Stevens', 'Clallam', 'Lewis',
              'Okanogan', 'Clark', 'Douglas', 'Jefferson', 'Cowlitz', 'Benton',
              'Klickitat', 'Grays Harbor', 'Asotin', 'San Juan', 'Franklin'
              ]
city = ['Seattle', 'Bothell', 'Yakima', 'Kirkland', 'Olympia',
       'Marysville', 'Kent', 'Woodinville', 'Coupeville', 'Bellevue',
       'Port Orchard', 'Mukilteo', 'Redmond', 'Rochester', 'Bremerton',
       'Poulsbo', 'Lake Stevens', 'Silverdale', 'Kingston', 'Enumclaw',
       'Auburn', 'Moxee', 'Tieton', 'Renton', 'Tukwila', 'Seatac',
       'Tumwater', 'Suquamish', 'Oak Harbor', 'Shoreline', 'Seabeck',
       'Sammamish', 'Issaquah', 'Monroe', 'Bainbridge Island', 'Yelm',
       'Kenmore', 'Burien', 'Stanwood', 'Arlington', 'Maple Valley',
       'Medina', 'Federal Way', 'Snohomish', 'Toppenish', 'Everett',
       'Lynnwood', 'Des Moines', 'Lacey', 'Covington', 'Selah', 'Edmonds',
       'Hansville', 'Tenino', 'Bellingham', 'Woodway', 'North Bend',
       'Puyallup', 'Pullman', 'Rainier', 'Mount Vernon', 'Cle Elum',
       'Dupont', 'Burlington', 'Spokane', 'Anacortes', 'La Conner',
       'Walla Walla', 'Duvall', 'Freeland', 'Wenatchee', 'Newcastle',
       'Quincy', 'Cashmere', 'Concrete', 'Soap Lake', 'Mill Creek',
       'Leavenworth', 'Moses Lake', 'Snoqualmie', 'Coulee City',
       'Sedro-Woolley', 'Bow', 'Ellensburg', 'Clinton', 'Buckley',
       'Camano Island', 'Rice', 'Port Angeles', 'Chewelah',
       'Mountlake Terrace', 'Vashon', 'Chehalis', 'Langley',
       'South Cle Elum', 'Royal City', 'Ephrata', 'Entiat', 'Carnation',
       'Pateros', 'Granite Falls', 'Brier', 'Colville', 'Vancouver',
       'Oroville', 'Graham', 'Waterville', 'La Center', 'Lakewood',
       'Brush Prairie', 'Port Townsend', 'Normandy Park', 'Woodland',
       'Olalla', 'Sequim', 'Pacific', 'Ariel', 'Longview',
       'Nine Mile Falls', 'Brinnon', 'Kalama', 'Lake Forest Park',
       'Washougal', 'Camas', 'Battle Ground', 'Beaux Arts', 'Port Ludlow',
       'University Place', 'Mercer Island', 'Silverlake', 'Kelso',
       'Ridgefield', 'Tacoma', 'Steilacoom', 'Cheney', 'Richland',
       'Clyde Hill', 'Lakebay', 'Fall City', 'Sunnyside', 'Castle Rock',
       'Naches', 'White Salmon', 'Grandview', 'Ocean Shores', 'Yacolt',
       'Amboy', 'Quilcene', 'Aberdeen', 'Sumner', 'Centralia',
       'Darrington', 'Kennewick', 'Nordland', 'Bingen', 'Gig Harbor',
       'Clarkston', 'Milton', 'Ravensdale', 'Bonney Lake', 'Tulalip',
       'Lake Tapps', 'Friday Harbor', 'Indianola', 'Granger', 'Pasco',
       'Sultan', 'Fox Island', 'Port Hadlock', 'Keyport',
       'Spokane Valley']
make = ['HYUNDAI', 'JEEP', 'TESLA', 'BMW', 'CHRYSLER', 'FORD', 'TOYOTA',
       'AUDI', 'NISSAN', 'KIA', 'CHEVROLET', 'VOLKSWAGEN', 'FIAT',
       'VOLVO', 'MINI', 'SMART', 'RIVIAN', 'HONDA', 'PORSCHE',
       'MITSUBISHI', 'SUBARU', 'POLESTAR', 'MERCEDES-BENZ', 'CADILLAC',
       'JAGUAR', 'LINCOLN', 'GENESIS', 'LUCID', 'LEXUS', 'FISKER',
       'MAZDA', 'LAND ROVER']

Model = ['KONA', 'GRAND CHEROKEE', 'MODEL 3', 'I3', 'PACIFICA', 'MODEL Y',
       'FUSION', 'PRIUS PRIME', 'E-TRON', 'LEAF', 'NIRO', 'X5', 'MODEL S',
       'VOLT', 'RAV4', 'C-MAX', 'E-GOLF', '500', 'BOLT EV', 'ID.4',
       '330E', 'A3', 'FOCUS', 'SORENTO', 'TUCSON', 'MODEL X', 'XC60',
       'SOUL', 'SPORTAGE', 'HARDTOP', 'WRANGLER', 'Q5 E', 'EQ FORTWO',
       'X3', 'R1S', 'Q5', 'CLARITY', 'F-150', 'XC90', 'CAYENNE',
       'RAV4 PRIME', 'SPARK', 'OPTIMA', 'R1T', 'ESCAPE', 'SOUL EV',
       'OUTLANDER', 'ROADSTER', 'FORTWO', 'MUSTANG MACH-E', '740E', 'EV6',
       'SOLTERRA', 'IX', 'BOLT EUV', 'IONIQ 5', 'I4', 'TRANSIT',
       'KONA ELECTRIC', 'PS2', 'EQB-CLASS', 'PRIUS PLUG-IN', 'SANTA FE',
       'TAYCAN', 'LYRIQ', 'EQS-CLASS SEDAN', 'I-PACE', '530E', 'I8',
       'XC40', 'COUNTRYMAN', 'S60', 'ELR', 'AVIATOR', 'IONIQ',
       'E-TRON GT', 'G80', 'IONIQ 6', 'ARIYA', 'GLC-CLASS', 'C40',
       'EQS-CLASS SUV', 'GV60', 'Q4', 'A7', 'E-TRON SPORTBACK', 'AIR',
       'B-CLASS', 'NX', 'GLE-CLASS', 'C-CLASS', 'RZ 450E', 'V60',
       'EQE-CLASS SUV', 'A8 E', 'BZ4X', 'PANAMERA',
       'FORTWO ELECTRIC DRIVE', 'SONATA', 'KARMA', 'CT6', 'CX-90',
       'PRIUS', 'ACCORD', 'CROSSTREK', 'S90', 'CORSAIR', 'RANGE ROVER',
       'I-MIEV', 'EDV', 'RS E-TRON GT']

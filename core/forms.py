from django import forms
from .models import Search


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = [
            'bandName',
            'genre',
            'country',
            'status',
            'yearCreationFrom',
            'yearCreationTo',
            'bandNotes',
            'themes',
            'location',
            'bandLabelName'
        ]


class OLDSearchForm(forms.Form):
    COUNTRY_CHOICES = [
        ("", "(Any)"),
        ("AF", "Afghanistan"),
        ("AX", "Åland Islands"),
        ("AL", "Albania"),
        ("DZ", "Algeria"),
        ("AS", "American Samoa"),
        ("AD", "Andorra"),
        ("AO", "Angola"),
        ("AI", "Anguilla"),
        ("AQ", "Antarctica"),
        ("AG", "Antigua and Barbuda"),
        ("AR", "Argentina"),
        ("AM", "Armenia"),
        ("AW", "Aruba"),
        ("AU", "Australia"),
        ("AT", "Austria"),
        ("AZ", "Azerbaijan"),
        ("BS", "Bahamas"),
        ("BH", "Bahrain"),
        ("BD", "Bangladesh"),
        ("BB", "Barbados"),
        ("BY", "Belarus"),
        ("BE", "Belgium"),
        ("BZ", "Belize"),
        ("BJ", "Benin"),
        ("BM", "Bermuda"),
        ("BT", "Bhutan"),
        ("BO", "Bolivia"),
        ("BQ", "Bonaire, Sint Eustatius and Saba"),
        ("BA", "Bosnia and Herzegovina"),
        ("BW", "Botswana"),
        ("BV", "Bouvet Island"),
        ("BR", "Brazil"),
        ("IO", "British Indian Ocean Territory"),
        ("BN", "Brunei"),
        ("BG", "Bulgaria"),
        ("BF", "Burkina Faso"),
        ("BI", "Burundi"),
        ("KH", "Cambodia"),
        ("CM", "Cameroon"),
        ("CA", "Canada"),
        ("CV", "Cape Verde"),
        ("KY", "Cayman Islands"),
        ("CF", "Central African Republic"),
        ("TD", "Chad"),
        ("CL", "Chile"),
        ("CN", "China"),
        ("CX", "Christmas Island"),
        ("CC", "Cocos (Keeling) Islands"),
        ("CO", "Colombia"),
        ("KM", "Comoros"),
        ("CD", "Congo, Democratic Republic of"),
        ("CG", "Congo, Republic of"),
        ("CK", "Cook Islands"),
        ("CR", "Costa Rica"),
        ("HR", "Croatia"),
        ("CU", "Cuba"),
        ("CW", "Curaçao"),
        ("CY", "Cyprus"),
        ("CZ", "Czechia"),
        ("DK", "Denmark"),
        ("DJ", "Djibouti"),
        ("DM", "Dominica"),
        ("DO", "Dominican Republic"),
        ("TL", "East Timor"),
        ("EC", "Ecuador"),
        ("EG", "Egypt"),
        ("SV", "El Salvador"),
        ("GQ", "Equatorial Guinea"),
        ("ER", "Eritrea"),
        ("EE", "Estonia"),
        ("SZ", "Eswatini"),
        ("ET", "Ethiopia"),
        ("FK", "Falkland Islands"),
        ("FO", "Faroe Islands"),
        ("FJ", "Fiji"),
        ("FI", "Finland"),
        ("FR", "France"),
        ("GF", "French Guiana"),
        ("PF", "French Polynesia"),
        ("TF", "French Southern Territories"),
        ("GA", "Gabon"),
        ("GM", "Gambia"),
        ("GE", "Georgia"),
        ("DE", "Germany"),
        ("GH", "Ghana"),
        ("GI", "Gibraltar"),
        ("GR", "Greece"),
        ("GL", "Greenland"),
        ("GD", "Grenada"),
        ("GP", "Guadeloupe"),
        ("GU", "Guam"),
        ("GT", "Guatemala"),
        ("GG", "Guernsey"),
        ("GN", "Guinea"),
        ("GW", "Guinea-Bissau"),
        ("GY", "Guyana"),
        ("HT", "Haiti"),
        ("HM", "Heard and McDonald Islands"),
        ("HN", "Honduras"),
        ("HK", "Hong Kong"),
        ("HU", "Hungary"),
        ("IS", "Iceland"),
        ("IN", "India"),
        ("ID", "Indonesia"),
        ("XX", "International"),
        ("IR", "Iran"),
        ("IQ", "Iraq"),
        ("IE", "Ireland"),
        ("IM", "Isle of Man"),
        ("IL", "Israel"),
        ("IT", "Italy"),
        ("CI", "Ivory Coast"),
        ("JM", "Jamaica"),
        ("JP", "Japan"),
        ("JE", "Jersey"),
        ("JO", "Jordan"),
        ("KZ", "Kazakhstan"),
        ("KE", "Kenya"),
        ("KI", "Kiribati"),
        ("KP", "Korea, North"),
        ("KR", "Korea, South"),
        ("KW", "Kuwait"),
        ("KG", "Kyrgyzstan"),
        ("LA", "Laos"),
        ("LV", "Latvia"),
        ("LB", "Lebanon"),
        ("LS", "Lesotho"),
        ("LR", "Liberia"),
        ("LY", "Libya"),
        ("LI", "Liechtenstein"),
        ("LT", "Lithuania"),
        ("LU", "Luxembourg"),
        ("MO", "Macau"),
        ("MG", "Madagascar"),
        ("MW", "Malawi"),
        ("MY", "Malaysia"),
        ("MV", "Maldives"),
        ("ML", "Mali"),
        ("MT", "Malta"),
        ("MH", "Marshall Islands"),
        ("MQ", "Martinique"),
        ("MR", "Mauritania"),
        ("MU", "Mauritius"),
        ("YT", "Mayotte"),
        ("MX", "Mexico"),
        ("FM", "Micronesia, Federated States of"),
        ("MD", "Moldova"),
        ("MC", "Monaco"),
        ("MN", "Mongolia"),
        ("ME", "Montenegro"),
        ("MS", "Montserrat"),
        ("MA", "Morocco"),
        ("MZ", "Mozambique"),
        ("MM", "Myanmar"),
        ("NA", "Namibia"),
        ("NR", "Nauru"),
        ("NP", "Nepal"),
        ("NL", "Netherlands"),
        ("NC", "New Caledonia"),
        ("NZ", "New Zealand"),
        ("NI", "Nicaragua"),
        ("NE", "Niger"),
        ("NG", "Nigeria"),
        ("NU", "Niue"),
        ("NF", "Norfolk Island"),
        ("MK", "North Macedonia"),
        ("MP", "Northern Mariana Islands"),
        ("NO", "Norway"),
        ("OM", "Oman"),
        ("PK", "Pakistan"),
        ("PW", "Palau"),
        ("PS", "Palestine"),
        ("PA", "Panama"),
        ("PG", "Papua New Guinea"),
        ("PY", "Paraguay"),
        ("PE", "Peru"),
        ("PH", "Philippines"),
        ("PN", "Pitcairn Island"),
        ("PL", "Poland"),
        ("PT", "Portugal"),
        ("PR", "Puerto Rico"),
        ("QA", "Qatar"),
        ("RE", "Reunion"),
        ("RO", "Romania"),
        ("RU", "Russia"),
        ("RW", "Rwanda"),
        ("BL", "Saint Barthélemy"),
        ("KN", "Saint Kitts & Nevis"),
        ("LC", "Saint Lucia"),
        ("MF", "Saint Martin (French part)"),
        ("PM", "Saint Pierre and Miquelon"),
        ("VC", "Saint Vincent and The Grenadines"),
        ("WS", "Samoa"),
        ("SM", "San Marino"),
        ("ST", "Sao Tome and Principe"),
        ("SA", "Saudi Arabia"),
        ("SN", "Senegal"),
        ("RS", "Serbia"),
        ("SC", "Seychelles"),
        ("SL", "Sierra Leone"),
        ("SG", "Singapore"),
        ("SX", "Sint Maarten (Dutch part)"),
        ("SK", "Slovakia"),
        ("SI", "Slovenia"),
        ("SB", "Solomon Islands"),
        ("SO", "Somalia"),
        ("ZA", "South Africa"),
        ("GS", "South Georgia & South Sandwich Islands"),
        ("SS", "South Sudan"),
        ("ES", "Spain"),
        ("LK", "Sri Lanka"),
        ("SH", "St Helena, Ascension & Tristan da Cunha"),
        ("SD", "Sudan"),
        ("SR", "Suriname"),
        ("SJ", "Svalbard"),
        ("SE", "Sweden"),
        ("CH", "Switzerland"),
        ("SY", "Syria"),
        ("TW", "Taiwan"),
        ("TJ", "Tajikistan"),
        ("TZ", "Tanzania"),
        ("TH", "Thailand"),
        ("TG", "Togo"),
        ("TK", "Tokelau"),
        ("TO", "Tonga"),
        ("TT", "Trinidad and Tobago"),
        ("TN", "Tunisia"),
        ("TR", "Turkey"),
        ("TM", "Turkmenistan"),
        ("TC", "Turks and Caicos Islands"),
        ("TV", "Tuvalu"),
        ("UM", "U.S. Minor Outlying Islands"),
        ("UG", "Uganda"),
        ("UA", "Ukraine"),
        ("AE", "United Arab Emirates"),
        ("GB", "United Kingdom"),
        ("US", "United States"),
        ("ZZ", "Unknown"),
        ("UY", "Uruguay"),
        ("UZ", "Uzbekistan"),
        ("VU", "Vanuatu"),
        ("VA", "Vatican City"),
        ("VE", "Venezuela"),
        ("VN", "Vietnam"),
        ("VG", "Virgin Islands (British)"),
        ("VI", "Virgin Islands (US)"),
        ("WF", "Wallis and Futuna"),
        ("EH", "Western Sahara"),
        ("YE", "Yemen"),
        ("ZM", "Zambia")
    ]
    STATUS_CHOICES = [
        ("", "(Any)"),
        ("1", "Active"),
        ("2", "On hold"),
        ("3", "Split-up"),
        ("4", "Unknown"),
        ("5", "Changed name"),
        ("6", "Disputed")
    ]
    bandName = forms.CharField(label='Band Name', max_length=200, required=False)
    genre = forms.CharField(label='Genre', max_length=200, required=False)
    country = forms.ChoiceField(label='Country', choices=COUNTRY_CHOICES, required=False)
    status = forms.ChoiceField(label='Status', choices=STATUS_CHOICES, required=False)
    yearCreationFrom = forms.IntegerField(label='From', required=False)
    yearCreationTo = forms.IntegerField(label='To', required=False)
    bandNotes = forms.CharField(label='Additional notes', max_length=300, required=False)
    themes = forms.CharField(label='Lyrical Themes', max_length=300, required=False)
    location = forms.CharField(label='City/state/province', max_length=200, required=False)
    bandLabelName = forms.CharField(label='Label', max_length=200, required=False)

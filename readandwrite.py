import requests
import json

countriessec = {
    {
        n: "Afghanistan",
        i: "af",
        d: "93"
    }, {
        n: "Aland Islands",
        i: "ax",
        d: "358"
    }, {
        n: "Albania",
        i: "al",
        d: "355"
    }, {
        n: "Algeria",
        i: "dz",
        d: "213"
    }, {
        n: "American Samoa",
        i: "as",
        d: "1684"
    }, {
        n: "Andorra",
        i: "ad",
        d: "376"
    }, {
        n: "Angola",
        i: "ao",
        d: "244"
    }, {
        n: "Anguilla",
        i: "ai",
        d: "1264"
    }, {
        n: "Antigua and Barbuda",
        i: "ag",
        d: "1268"
    }, {
        n: "Argentina",
        i: "ar",
        d: "54"
    }, {
        n: "Armenia",
        i: "am",
        d: "374"
    }, {
        n: "Aruba",
        i: "aw",
        d: "297"
    }, {
        n: "Australia",
        i: "au",
        d: "61"
    }, {
        n: "Austria",
        i: "at",
        d: "43"
    }, {
        n: "Azerbaijan",
        i: "az",
        d: "994"
    }, {
        n: "Bahamas",
        i: "bs",
        d: "1242"
    }, {
        n: "Bahrain",
        i: "bh",
        d: "973"
    }, {
        n: "Bangladesh",
        i: "bd",
        d: "880"
    }, {
        n: "Barbados",
        i: "bb",
        d: "1246"
    }, {
        n: "Belarus",
        i: "by",
        d: "375"
    }, {
        n: "Belgium",
        i: "be",
        d: "32"
    }, {
        n: "Belize",
        i: "bz",
        d: "501"
    }, {
        n: "Benin",
        i: "bj",
        d: "229"
    }, {
        n: "Bermuda",
        i: "bm",
        d: "1441"
    }, {
        n: "Bhutan",
        i: "bt",
        d: "975"
    }, {
        n: "Bolivia",
        i: "bo",
        d: "591"
    }, {
        n: "Bosnia and Herzegovina",
        i: "ba",
        d: "387"
    }, {
        n: "Botswana",
        i: "bw",
        d: "267"
    }, {
        n: "Brazil",
        i: "br",
        d: "55"
    }, {
        n: "British Indian Ocean Territory",
        i: "io",
        d: "246"
    }, {
        n: "British Virgin Islands",
        i: "vg",
        d: "1284"
    }, {
        n: "Brunei",
        i: "bn",
        d: "673"
    }, {
        n: "Bulgaria",
        i: "bg",
        d: "359"
    }, {
        n: "Burkina Faso",
        i: "bf",
        d: "226"
    }, {
        n: "Burundi",
        i: "bi",
        d: "257"
    },
    {
        n: "Cambodia",
        i: "kh",
        d: "855"
    }, {
        n: "Cameroon",
        i: "cm",
        d: "237"
    },
    {
        n: "Canada",
        i: "ca",
        d: "1"
    },
    {
        n: "Cape Verde",
        i: "cv",
        d: "238"
    }, {
        n: "Caribbean Netherlands",
        i: "bq",
        d: "5997"
    }, {
        n: "Cayman Islands",
        i: "ky",
        d: "1345"
    }, {
        n: "Central African Republic",
        i: "cf",
        d: "236"
    }, {
        n: "Chad",
        i: "td",
        d: "235"
    },
    {
        n: "Chile",
        i: "cl",
        d: "56"
    }, {
        n: "China",
        i: "cn",
        d: "86"
    },
    {
        n: "Christmas Island",
        i: "cx",
        d: "61"
    }, {
        n: "Cocos (Keeling) Islands",
        i: "cc",
        d: "61"
    }, {
        n: "Colombia",
        i: "co",
        d: "57"
    }, {
        n: "Comoros",
        i: "km",
        d: "269"
    }, {
        n: "Congo (DRC)",
        i: "cd",
        d: "243"
    }, {
        n: "Congo (Republic)",
        i: "cg",
        d: "242"
    }, {
        n: "Cook Islands",
        i: "ck",
        d: "682"
    }, {
        n: "Costa Rica",
        i: "cr",
        d: "506"
    }, {
        n: "Côte d’Ivoire",
        i: "ci",
        d: "225"
    }, {
        n: "Croatia",
        i: "hr",
        d: "385"
    }, {
        n: "Cuba",
        i: "cu",
        d: "53"
    }, {
        n: "Curaçao",
        i: "cw",
        d: "5999"
    }, {
        n: "Cyprus",
        i: "cy",
        d: "357"
    }, {
        n: "Czech Republic",
        i: "cz",
        d: "420"
    }, {
        n: "Denmark",
        i: "dk",
        d: "45"
    }, {
        n: "Djibouti",
        i: "dj",
        d: "253"
    }, {
        n: "Dominica",
        i: "dm",
        d: "1767"
    }, {
        n: "Dominican Republic",
        i: "do",
        d: "1809"
    }, {
        n: "Ecuador",
        i: "ec",
        d: "593"
    }, {
        n: "Egypt",
        i: "eg",
        d: "20"
    }, {
        n: "El Salvador",
        i: "sv",
        d: "503"
    }, {
        n: "Equatorial Guinea",
        i: "gq",
        d: "240"
    }, {
        n: "Eritrea",
        i: "er",
        d: "291"
    }, {
        n: "Estonia",
        i: "ee",
        d: "372"
    }, {
        n: "Ethiopia",
        i: "et",
        d: "251"
    }, {
        n: "Falkland Islands",
        i: "fk",
        d: "500"
    }, {
        n: "Faroe Islands",
        i: "fo",
        d: "298"
    }, {
        n: "Fiji",
        i: "fj",
        d: "679"
    }, {
        n: "Finland",
        i: "fi",
        d: "358"
    }, {
        n: "France",
        i: "fr",
        d: "33"
    }, {
        n: "French Guiana",
        i: "gf",
        d: "594"
    }, {
        n: "French Polynesia",
        i: "pf",
        d: "689"
    }, {
        n: "Gabon",
        i: "ga",
        d: "241"
    }, {
        n: "Gambia",
        i: "gm",
        d: "220"
    }, {
        n: "Georgia",
        i: "ge",
        d: "995"
    }, {
        n: "Germany",
        i: "de",
        d: "49"
    }, {
        n: "Ghana",
        i: "gh",
        d: "233"
    }, {
        n: "Gibraltar",
        i: "gi",
        d: "350"
    }, {
        n: "Greece",
        i: "gr",
        d: "30"
    }, {
        n: "Greenland",
        i: "gl",
        d: "299"
    }, {
        n: "Grenada",
        i: "gd",
        d: "1473"
    }, {
        n: "Guadeloupe",
        i: "gp",
        d: "590"
    }, {
        n: "Guam",
        i: "gu",
        d: "1671"
    }, {
        n: "Guatemala",
        i: "gt",
        d: "502"
    }, {
        n: "Guernsey",
        i: "gg",
        d: "44"
    }, {
        n: "Guinea",
        i: "gn",
        d: "224"
    }, {
        n: "Guinea-Bissau",
        i: "gw",
        d: "245"
    }, {
        n: "Guyana",
        i: "gy",
        d: "592"
    }, {
        n: "Haiti",
        i: "ht",
        d: "509"
    }, {
        n: "Honduras",
        i: "hn",
        d: "504"
    }, {
        n: "Hong Kong",
        i: "hk",
        d: "852"
    }, {
        n: "Hungary",
        i: "hu",
        d: "36"
    }, {
        n: "Iceland",
        i: "is",
        d: "354"
    }, {
        n: "India",
        i: "in",
        d: "91"
    }, {
        n: "Indonesia",
        i: "id",
        d: "62"
    }, {
        n: "Iran",
        i: "ir",
        d: "98"
    }, {
        n: "Iraq",
        i: "iq",
        d: "964"
    }, {
        n: "Ireland",
        i: "ie",
        d: "353"
    }, {
        n: "Isle of Man",
        i: "im",
        d: "44"
    }, {
        n: "Israel",
        i: "il",
        d: "972"
    }, {
        n: "Italy",
        i: "it",
        d: "39"
    }, {
        n: "Jamaica",
        i: "jm",
        d: "1876"
    }, {
        n: "Japan",
        i: "jp",
        d: "81"
    }, {
        n: "Jersey",
        i: "je",
        d: "44"
    }, {
        n: "Jordan",
        i: "jo",
        d: "962"
    }, {
        n: "Kazakhstan",
        i: "kz",
        d: "7"
    }, {
        n: "Kenya",
        i: "ke",
        d: "254"
    }, {
        n: "Kiribati",
        i: "ki",
        d: "686"
    }, {
        n: "Kosovo",
        i: "xk",
        d: "377"
    }, {
        n: "Kuwait",
        i: "kw",
        d: "965"
    }, {
        n: "Kyrgyzstan",
        i: "kg",
        d: "996"
    }, {
        n: "Laos",
        i: "la",
        d: "856"
    }, {
        n: "Latvia",
        i: "lv",
        d: "371"
    }, {
        n: "Lebanon",
        i: "lb",
        d: "961"
    }, {
        n: "Lesotho",
        i: "ls",
        d: "266"
    }, {
        n: "Liberia",
        i: "lr",
        d: "231"
    }, {
        n: "Libya",
        i: "ly",
        d: "218"
    }, {
        n: "Liechtenstein",
        i: "li",
        d: "423"
    }, {
        n: "Lithuania",
        i: "lt",
        d: "370"
    }, {
        n: "Luxembourg",
        i: "lu",
        d: "352"
    }, {
        n: "Macau",
        i: "mo",
        d: "853"
    }, {
        n: "Macedonia",
        i: "mk",
        d: "389"
    }, {
        n: "Madagascar",
        i: "mg",
        d: "261"
    }, {
        n: "Malawi",
        i: "mw",
        d: "265"
    }, {
        n: "Malaysia",
        i: "my",
        d: "60"
    }, {
        n: "Maldives",
        i: "mv",
        d: "960"
    }, {
        n: "Mali",
        i: "ml",
        d: "223"
    }, {
        n: "Malta",
        i: "mt",
        d: "356"
    }, {
        n: "Marshall Islands",
        i: "mh",
        d: "692"
    }, {
        n: "Martinique",
        i: "mq",
        d: "596"
    }, {
        n: "Mauritania",
        i: "mr",
        d: "222"
    }, {
        n: "Mauritius",
        i: "mu",
        d: "230"
    }, {
        n: "Mayotte",
        i: "yt",
        d: "262"
    }, {
        n: "Mexico",
        i: "mx",
        d: "52"
    }, {
        n: "Micronesia",
        i: "fm",
        d: "691"
    }, {
        n: "Moldova",
        i: "md",
        d: "373"
    }, {
        n: "Monaco",
        i: "mc",
        d: "377"
    }, {
        n: "Mongolia",
        i: "mn",
        d: "976"
    }, {
        n: "Montenegro",
        i: "me",
        d: "382"
    }, {
        n: "Montserrat",
        i: "ms",
        d: "1664"
    }, {
        n: "Morocco",
        i: "ma",
        d: "212"
    }, {
        n: "Mozambique",
        i: "mz",
        d: "258"
    }, {
        n: "Myanmar",
        i: "mm",
        d: "95"
    }, {
        n: "Namibia",
        i: "na",
        d: "264"
    }, {
        n: "Nauru",
        i: "nr",
        d: "674"
    }, {
        n: "Nepal",
        i: "np",
        d: "977"
    }, {
        n: "Netherlands",
        i: "nl",
        d: "31"
    }, {
        n: "New Caledonia",
        i: "nc",
        d: "687"
    }, {
        n: "New Zealand",
        i: "nz",
        d: "64"
    }, {
        n: "Nicaragua",
        i: "ni",
        d: "505"
    }, {
        n: "Niger",
        i: "ne",
        d: "227"
    }, {
        n: "Nigeria",
        i: "ng",
        d: "234"
    }, {
        n: "Niue",
        i: "nu",
        d: "683"
    }, {
        n: "Norfolk Island",
        i: "nf",
        d: "672"
    }, {
        n: "North Korea",
        i: "kp",
        d: "850"
    }, {
        n: "Northern Mariana Islands",
        i: "mp",
        d: "1670"
    }, {
        n: "Norway",
        i: "no",
        d: "47"
    }, {
        n: "Oman",
        i: "om",
        d: "968"
    },
    {
        n: "Pakistan",
        i: "pk",
        d: "92"
    }
    , {
        n: "Palau",
        i: "pw",
        d: "680"
    }, {
        n: "Palestine",
        i: "ps",
        d: "970"
    }, {
        n: "Panama",
        i: "pa",
        d: "507"
    }, {
        n: "Papua New Guinea",
        i: "pg",
        d: "675"
    }, {
        n: "Paraguay",
        i: "py",
        d: "595"
    }, {
        n: "Peru",
        i: "pe",
        d: "51"
    }, {
        n: "Philippines",
        i: "ph",
        d: "63"
    }, {
        n: "Pitcairn Islands",
        i: "pn",
        d: "64"
    }, {
        n: "Poland",
        i: "pl",
        d: "48"
    }, {
        n: "Portugal",
        i: "pt",
        d: "351"
    }, {
        n: "Puerto Rico",
        i: "pr",
        d: "1787"
    }, {
        n: "Qatar",
        i: "qa",
        d: "974"
    }, {
        n: "Réunion",
        i: "re",
        d: "262"
    }, {
        n: "Romania",
        i: "ro",
        d: "40"
    }, {
        n: "Russia",
        i: "ru",
        d: "7"
    }, {
        n: "Rwanda",
        i: "rw",
        d: "250"
    }, {
        n: "Saint Barthélemy",
        i: "bl",
        d: "590"
    }, {
        n: "Saint Helena",
        i: "sh",
        d: "290"
    }, {
        n: "Saint Kitts and Nevis",
        i: "kn",
        d: "1869"
    }, {
        n: "Saint Lucia",
        i: "lc",
        d: "1758"
    }, {
        n: "Saint Martin",
        i: "mf",
        d: "590"
    }, {
        n: "Saint Pierre & Miquelon",
        i: "pm",
        d: "508"
    }, {
        n: "Saint Vincent & the Grenadines",
        i: "vc",
        d: "1784"
    }, {
        n: "Samoa",
        i: "ws",
        d: "685"
    }, {
        n: "San Marino",
        i: "sm",
        d: "378"
    }, {
        n: "São Tomé and Príncipe",
        i: "st",
        d: "239"
    }, {
        n: "Saudi Arabia",
        i: "sa",
        d: "966"
    }, {
        n: "Senegal",
        i: "sn",
        d: "221"
    }, {
        n: "Serbia",
        i: "rs",
        d: "381"
    }, {
        n: "Seychelles",
        i: "sc",
        d: "248"
    }, {
        n: "Sierra Leone",
        i: "sl",
        d: "232"
    }, {
        n: "Singapore",
        i: "sg",
        d: "65"
    }, {
        n: "Sint Maarten",
        i: "sx",
        d: "1721"
    }, {
        n: "Slovakia",
        i: "sk",
        d: "421"
    }, {
        n: "Slovenia",
        i: "si",
        d: "386"
    }, {
        n: "Solomon Islands",
        i: "sb",
        d: "677"
    }, {
        n: "Somalia",
        i: "so",
        d: "252"
    }, {
        n: "South Africa",
        i: "za",
        d: "27"
    }, {
        n: "South Georgia & South Sandwich",
        i: "gs",
        d: "500"
    }, {
        n: "South Korea",
        i: "kr",
        d: "82"
    }, {
        n: "South Sudan",
        i: "ss",
        d: "211"
    }, {
        n: "Spain",
        i: "es",
        d: "34"
    }, {
        n: "Sri Lanka",
        i: "lk",
        d: "94"
    }, {
        n: "Sudan",
        i: "sd",
        d: "249"
    }, {
        n: "Suriname",
        i: "sr",
        d: "597"
    }, {
        n: "Svalbard and Jan Mayen",
        i: "sj",
        d: "4779"
    }, {
        n: "Swaziland",
        i: "sz",
        d: "268"
    }, {
        n: "Sweden",
        i: "se",
        d: "46"
    }, {
        n: "Switzerland",
        i: "ch",
        d: "41"
    }, {
        n: "Syria",
        i: "sy",
        d: "963"
    }, {
        n: "Taiwan",
        i: "tw",
        d: "886"
    }, {
        n: "Tajikistan",
        i: "tj",
        d: "992"
    }, {
        n: "Tanzania",
        i: "tz",
        d: "255"
    }, {
        n: "Thailand",
        i: "th",
        d: "66"
    }, {
        n: "Timor-Leste",
        i: "tl",
        d: "670"
    }, {
        n: "Togo",
        i: "tg",
        d: "228"
    }, {
        n: "Tokelau",
        i: "tk",
        d: "690"
    }, {
        n: "Tonga",
        i: "to",
        d: "676"
    }, {
        n: "Trinidad and Tobago",
        i: "tt",
        d: "1868"
    }, {
        n: "Tunisia",
        i: "tn",
        d: "216"
    }, {
        n: "Turkey",
        i: "tr",
        d: "90"
    }, {
        n: "Turkmenistan",
        i: "tm",
        d: "993"
    }, {
        n: "Turks and Caicos Islands",
        i: "tc",
        d: "1649"
    }, {
        n: "Tuvalu",
        i: "tv",
        d: "688"
    }, {
        n: "Uganda",
        i: "ug",
        d: "256"
    }, {
        n: "Ukraine",
        i: "ua",
        d: "380"
    }, {
        n: "United Arab Emirates",
        i: "ae",
        d: "971"
    }, {
        n: "United Kingdom",
        i: "gb",
        d: "44"
    }
    , {
        n: "United States",
        i: "us",
        d: "1"
    }
    , {
        n: "U.S. Virgin Islands",
        i: "vi",
        d: "1340"
    }, {
        n: "Uruguay",
        i: "uy",
        d: "598"
    }, {
        n: "Uzbekistan",
        i: "uz",
        d: "998"
    }, {
        n: "Vanuatu",
        i: "vu",
        d: "678"
    }, {
        n: "Vatican City",
        i: "va",
        d: "379"
    }, {
        n: "Venezuela",
        i: "ve",
        d: "58"
    }, {
        n: "Vietnam",
        i: "vn",
        d: "84"
    }, {
        n: "Wallis and Futuna",
        i: "wf",
        d: "681"
    }, {
        n: "Western Sahara",
        i: "eh",
        d: "212"
    }, {
        n: "Yemen",
        i: "ye",
        d: "967"
    }, {
        n: "Zambia",
        i: "zm",
        d: "260"
    }, {
        n: "Zimbabwe",
        i: "zw",
        d: "263"
    }
}




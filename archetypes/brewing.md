---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: false
categories:
- brewing
tags: []
description: ""
preview: ""
qr: ""
has_qr: yes
brew_brewfather_url: ""  # Brewfather link
brew_date: ""  # Brew date
brew_fermentation_end_date: ""  # Fermentation end date
brew_og: ""  # Original Gravity
brew_fg: ""  # Final Gravity
brew_abv: ""  # Alcohol By Volume
brew_ibu: ""  # International Bitterness Units
brew_srm: ""  # Standard Reference Method (color)
brew_yeast: ""  # Yeast used
brew_ingredients:
  - name: ""
    amount: ""
    type: ""  # e.g., malt, hops, yeast, adjuncts
    use: ""  # e.g., mash, boil, primary, secondary
brew_notes: ""  # Any additional notes about the brewing process
brew_tasting_notes: ""  # Notes about the taste, aroma, and appearance
---

<!-- Add your brewing session content here -->

## Brewing Session Details

- **Brewfather URL:** {{ .Params.brew_brewfather_url }}
- **Brew Date:** {{ .Params.brew_date }}
- **Fermentation End Date:** {{ .Params.brew_fermentation_end_date }}
- **Original Gravity (OG):** {{ .Params.brew_og }}
- **Final Gravity (FG):** {{ .Params.brew_fg }}
- **Alcohol By Volume (ABV):** {{ .Params.brew_abv }}
- **International Bitterness Units (IBU):** {{ .Params.brew_ibu }}
- **Standard Reference Method (SRM):** {{ .Params.brew_srm }}
- **Yeast:** {{ .Params.brew_yeast }}

## Ingredients

{{ range .Params.brew_ingredients }}

- **{{ .name }}:** {{ .amount }} ({{ .type }}, {{ .use }})
{{ end }}

## Brewing Notes

{{ .Params.brew_notes }}

## Tasting Notes

{{ .Params.brew_tasting_notes }}

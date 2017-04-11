# Pokémon TCG SDK

[![PyPI version](https://badge.fury.io/py/pokemontcgsdk.svg)](https://badge.fury.io/py/pokemontcgsdk)
[![Build Status](https://travis-ci.org/PokemonTCG/pokemon-tcg-sdk-python.svg?branch=master)](https://travis-ci.org/PokemonTCG/pokemon-tcg-sdk-python)
[![Requirements Status](https://requires.io/github/PokemonTCG/pokemon-tcg-sdk-python/requirements.svg?branch=master)](https://requires.io/github/PokemonTCG/pokemon-tcg-sdk-python/requirements/?branch=master)
[![Code Climate](https://codeclimate.com/github/PokemonTCG/pokemon-tcg-sdk-python/badges/gpa.svg)](https://codeclimate.com/github/PokemonTCG/pokemon-tcg-sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/PokemonTCG/pokemon-tcg-sdk-python/badge.svg?branch=master)](https://coveralls.io/github/PokemonTCG/pokemon-tcg-sdk-python?branch=master)

This is the Pokémon TCG SDK Python implementation. It is a wrapper around the Pokémon TCG API of [pokemontcg.io](http://pokemontcg.io/).

## Requirements
Python 3 is currently the only supported version for the sdk. More specifically, the package was developed using Python 3.4.

## Installation

Using pip:

    pip install pokemontcgsdk

## Usage

Import (Card and Set will be most used)

    from pokemontcgsdk import Card
    from pokemontcgsdk import Set
    from pokemontcgsdk import Type
    from pokemontcgsdk import Supertype
    from pokemontcgsdk import Subtype

### Classes

    Card
    Set
    Type
    Supertype
    Subtype

### Properties Per Class

#### Card

    id
    name
    national_pokedex_number
    image_url
    image_url_hi_res
    subtype
    supertype
    ability
    ancient_trait
    hp
    number
    artist
    rarity
    series
    set
    set_code
    retreat_cost
    text
    types
    attacks
    weaknesses
    resistances

#### Set

    code
    name
    series
    total_cards
    standard_legal
    expanded_legal
    release_date

### Functions Available

#### Find a card by id

    card = Card.find('xy1-1')

#### Filter Cards via query parameters

    cards = Card.where(set='generations').where(supertype='pokemon').all()
    
#### Find all cards (will take awhile)

    cards = Card.all()
    
#### Get all cards, but only a specific page of data

    cards = Card.where(page=5).where(pageSize=100).all()
    
#### Find a set by code

    set = Set.find('base1')
    
#### Filter sets via query parameters

    sets = Set.where(standardLegal=true).all()
    
#### Get all Sets

    sets = Set.all()
    
#### Get all Types

    types = Type.all()

#### Get all Subtypes

    subtypes = Subtype.all()

#### Get all Supertypes

    supertypes = Supertype.all()

## Contributing

1. Fork it ( https://github.com/[my-github-username]/pokemon-tcg-sdk-python/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

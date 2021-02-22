# Pokémon TCG SDK

[![PyPI version](https://badge.fury.io/py/pokemontcgsdk.svg)](https://badge.fury.io/py/pokemontcgsdk)
[![Build Status](https://travis-ci.org/PokemonTCG/pokemon-tcg-sdk-python.svg?branch=master)](https://travis-ci.org/PokemonTCG/pokemon-tcg-sdk-python)
[![Requirements Status](https://requires.io/github/PokemonTCG/pokemon-tcg-sdk-python/requirements.svg?branch=master)](https://requires.io/github/PokemonTCG/pokemon-tcg-sdk-python/requirements/?branch=master)
[![Code Climate](https://codeclimate.com/github/PokemonTCG/pokemon-tcg-sdk-python/badges/gpa.svg)](https://codeclimate.com/github/PokemonTCG/pokemon-tcg-sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/PokemonTCG/pokemon-tcg-sdk-python/badge.svg?branch=master)](https://coveralls.io/github/PokemonTCG/pokemon-tcg-sdk-python?branch=master)

This is the Pokémon TCG SDK Python implementation. It is a wrapper around the Pokémon TCG API of [pokemontcg.io](http://pokemontcg.io/).

## Requirements
Python 3 is currently the only supported version for the sdk. More specifically, the package was developed using Python 3.9.

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
    from pokemontcgsdk import Rarity


### API-Key

In order to set an API Key from https://dev.pokemontcg.io, just set the environment variable:

    export POKEMONTCG_IO_API_KEY='12345678-1234-1234-1234-123456789ABC'

### Classes

    Card
    Set
    Type
    Supertype
    Subtype
    Rarity

### Properties Per Class

#### Card

    abilities
    artist
    ancientTrait
    attacks
    convertedRetreatCost
    evolvesFrom
    flavorText
    hp
    id
    images
    legalities
    name
    nationalPokedexNumbers
    number
    rarity
    resistances
    retreatCost
    rules
    set
    subtypes
    supertype
    tcgplayer
    types
    weaknesses

#### Set

    id
    images
    legalities
    name
    printedTotal
    ptcgoCode
    releaseDate
    series
    total
    updatedAt

### Functions Available

#### Find a card by id

    card = Card.find('xy1-1')

#### Filter Cards via query parameters

    cards = Card.where(q='set.name:generations supertype:pokemon')
    
#### Find all cards (will take awhile)

    cards = Card.all()
    
#### Get all cards, but only a specific page of data

    cards = Card.where(page=5, pageSize=250)
    
#### Find a set by code

    set = Set.find('base1')
    
#### Filter sets via query parameters

    sets = Set.where(q='legalities.standard:legal')
    
#### Get all Sets

    sets = Set.all()
    
#### Get all Types

    types = Type.all()

#### Get all Subtypes

    subtypes = Subtype.all()

#### Get all Supertypes

    supertypes = Supertype.all()

#### Get all Rarities

    rarities = Rarity.all()

## Contributing

1. Fork it ( https://github.com/[my-github-username]/pokemon-tcg-sdk-python/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Setup the development environment (`make setup`)
4. Make, Develop, and commit your changes! (`git commit -am 'Add some feature'`)
5. Run tests! (`make test`)
6. Push to the branch (`git push origin my-new-feature`)
7. Create a new Pull Request

## Developing

### Running Tests

    make test
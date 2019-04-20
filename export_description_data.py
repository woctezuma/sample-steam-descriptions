import json
import re

import steamspypi


def get_pycharm_project_root():
    pycharm_project_root = '../'

    return pycharm_project_root


def get_app_details_folder():
    base_folder_name = 'steam-api/data/appdetails/'
    app_details_folder = get_pycharm_project_root() + base_folder_name

    return app_details_folder


def get_app_details_file_name(app_id):
    base_file_name = 'appID_' + str(app_id) + '.json'
    app_details_file_name = get_app_details_folder() + base_file_name

    return app_details_file_name


def load_app_details(app_id):
    with open(get_app_details_file_name(app_id), 'r', encoding='utf8') as f:
        app_details = json.load(f)

    return app_details


def get_steamspy_catalog():
    steamspy_data = steamspypi.load()
    steamspy_catalog = set(int(app_id) for app_id in steamspy_data.keys())

    return steamspy_catalog


def get_data_folder():
    data_folder = 'data/'

    return data_folder


def get_json_aggregate_file_name():
    aggregate_file_name = get_data_folder() + 'aggregate.json'

    return aggregate_file_name


def get_txt_output_file_name():
    output_text_file_name = get_data_folder() + 'concatenated_store_descriptions.txt'

    return output_text_file_name


def aggregate_game_descriptions_from_steam_data(output_filename=None,
                                                verbose=True):
    # Code inspired from: https://github.com/woctezuma/steam-api/blob/master/aggregate_game_text_descriptions.py

    print('Aggregating game descriptions into a JSON file')

    if output_filename is None:
        output_filename = get_json_aggregate_file_name()

    aggregate = dict()

    # Variable used for debugging
    app_id_errors = list()

    # Label for the text below the banner on the store page. If empty, 'about_the_game' is used.
    game_header_label = 'short_description'
    # Label for the text in the section called 'About the game' on the store page
    game_description_label = 'about_the_game'
    # Label for:
    # - any text ABOVE the section called 'About the game', e.g. an advertisement for another game by the same dev,
    # - a separator, typically: '<br><h1>About the Game</h1>'
    # - the text in the section called 'About the game' on the store page.
    game_detailed_description_label = 'detailed_description'

    for app_id in sorted(get_steamspy_catalog(), key=int):
        try:
            app_details = load_app_details(app_id)
        except FileNotFoundError:
            if verbose:
                print('App details not found for appID = {}'.format(app_id))
                app_id_errors.append(app_id)
            continue

        try:
            app_name = app_details['name']
        except KeyError:
            if verbose:
                print('Name not found for appID = {}'.format(app_id))
                app_id_errors.append(app_id)
            continue
        except TypeError:
            if verbose:
                print('File empty for appID = {}'.format(app_id))
                app_id_errors.append(app_id)
            continue

        try:
            app_type = app_details['type']
        except KeyError:
            if verbose:
                print('Missing type for appID = {} ({})'.format(app_id, app_name))
                app_id_errors.append(app_id)
            continue

        if app_type == 'game':
            try:
                supported_languages = app_details['supported_languages']
            except KeyError:
                if verbose:
                    print('Missing information regarding language support for appID = {} ({})'.format(app_id, app_name))
                    app_id_errors.append(app_id)
                continue

            parsed_supported_languages = re.split(r'\W+', supported_languages)
            if 'English' in parsed_supported_languages:

                app_header = app_details[game_header_label]
                app_description = app_details[game_description_label]
                app_detailed_description = app_details[game_detailed_description_label]

                if verbose:
                    if app_description != app_detailed_description:
                        print('Descriptions differ for appID = {} ({})'.format(app_id, app_name))

                app_text = app_header + ' ' + app_description + ' ' + app_detailed_description
                app_text = app_text.strip()

                try:
                    app_genres = [genre['description'] for genre in app_details['genres']]
                except KeyError:
                    print('Missing genre description for appID = {} ({})'.format(app_id, app_name))
                    app_genres = []

                try:
                    app_categories = [categorie['description'] for categorie in app_details['categories']]
                except KeyError:
                    print('Missing categorie description for appID = {} ({})'.format(app_id, app_name))
                    app_categories = []

                if len(app_text) > 0:
                    aggregate[app_id] = dict()
                    aggregate[app_id]['name'] = app_name
                    aggregate[app_id]['header'] = app_header
                    aggregate[app_id]['description'] = app_description
                    aggregate[app_id]['detailed_description'] = app_detailed_description
                    aggregate[app_id]['genres'] = app_genres
                    aggregate[app_id]['categories'] = app_categories
            else:
                if verbose:
                    print('English not supported for appID = {} ({})'.format(app_id, app_name))
                continue

    if verbose:
        print('\nList of appIDs which were associated with erroneous or incomplete JSON app details:\n')
        print(app_id_errors)

    with open(output_filename, 'w', encoding='utf8') as f:
        json.dump(aggregate, f)

    return aggregate


def trim_description_content(description_content):
    # Remove empty lines

    description_content_chunks = [
        line.strip() for line in description_content.split('\n')
        if len(line.strip()) > 0
    ]

    trimmed_description_content = '\n'.join(description_content_chunks)

    return trimmed_description_content


def concatenate_description_data(output_file_name=None,
                                 aggregate=None,
                                 description_label=None,
                                 remove_empty_lines=True):
    print('Concatenating game descriptions into a TXT file')

    if output_file_name is None:
        output_file_name = get_txt_output_file_name()

    if aggregate is None:
        input_filename = get_json_aggregate_file_name()

        with open(input_filename, 'r', encoding='utf8') as f:
            aggregate = json.load(f)

    if description_label is None:
        # The label can be: i) 'header', ii) 'description', iii) 'detailed_description'.
        description_label = 'description'

    store_descriptions = []

    for app_id in sorted(aggregate.keys(), key=int):
        description_content = aggregate[app_id][description_label]

        if remove_empty_lines:
            trimmed_description_content = trim_description_content(description_content)
        else:
            trimmed_description_content = description_content

        if len(trimmed_description_content) > 0:
            store_descriptions.append(trimmed_description_content)

    line_separator = '\n'

    with open(output_file_name, 'w', encoding='utf8') as f:
        print(line_separator.join(store_descriptions), file=f)

    return


if __name__ == '__main__':
    aggregate_game_descriptions_from_steam_data()
    concatenate_description_data(description_label='description')

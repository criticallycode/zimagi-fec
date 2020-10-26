from systems.plugins.index import BaseProvider
from utility.data import ensure_list

import psycopg2


class Provider(BaseProvider('source', 'committee_db')):

    def __init__(self, type, name, command, id, config):
        super().__init__(type, name, command, id, config)

        self.config_facade = self.facade_index['config']
        self.conn = psycopg2.connect(
            host = config_facade.retrieve(self.field_host).value,
            database = config_facade.retrieve(self.field_database).value,
            user = config_facade.retrieve(self.field_user).value,
            password = config_facade.retrieve(self.field_password).value,
        )
        self.cursor = self.conn.cursor()


    def item_columns(self):
        return [
            'year',
            'committee_id',
            'name',
            'type',
            'designation',
            'filing_frequency',
            'state_id',
            'party_id',
            'party_name',
            'candidate_ids'
        ]

    def load_contexts(self):
        candidates = list(self.facade_index['candidate'].field_values('candidate_id'))
        contexts = []
        for year in ensure_list(self.field_years):
            for candidate_id in candidates:
                contexts.append({
                    'year': year,
                    'candidate_id': candidate_id
                })
        return contexts

    def load_items(self, context):

        return Committee.fetch(
            candidate_id = [ context['candidate_id'] ],
            year = [ context['year'] ],
            q = ensure_list(self.field_committees, True),
            committee_type = ensure_list(self.field_type_codes, True),
            party = ensure_list(self.field_party_codes, True),
            per_page = self.page_count
        )

    def load_item(self, committee, context):
        cycle_info = self._find_most_recent_year(committee.cycles, context['year'])
        return [
            cycle_info['year'],
            committee.committee_id,
            committee.name.strip().title(),
            committee.committee_type_full.title() if committee.committee_type_full else None,
            committee.designation_full.title() if committee.designation_full else None,
            committee.filing_frequency,
            committee.state,
            committee.party,
            committee.party_full.title() if committee.party_full else None,
            ",".join(committee.candidate_ids)
        ]
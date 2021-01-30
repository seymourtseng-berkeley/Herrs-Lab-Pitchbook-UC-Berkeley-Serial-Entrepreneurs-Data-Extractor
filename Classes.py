class SerialEntrepreneur:
    def __init__(self, id, full_name, last_name, first_name,
                 primary_position, primary_company, board_seats,
                 roles, deal_roles, phone, email, location,
                 address_line1, address_line2, city, state,
                 post_code, country, fax, biography, pitchbook_link):
        self.ID = id
        self.full_name = full_name
        self.last_name = last_name
        self.first_name = first_name
        self.primary_position = primary_position
        self.primary_company = primary_company
        self.board_seats = board_seats
        self.roles = roles
        self.deal_roles = deal_roles
        self.phone = phone
        self.email = email
        self.location = location
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.state = state
        self.post_code = post_code
        self.country = country
        self.full_address = self.get_full_address()
        self.fax = fax
        self.biography = biography
        self.pitchbook_link = pitchbook_link

    def get_full_address(self):
        full_address = self.address_line1 + ", " + self.city + \
                       ", " + self.state + " " + self.post_code +\
                       ", " + self.country
        return full_address



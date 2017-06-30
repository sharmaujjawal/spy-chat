from datetime import datetime

class user_detail:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class Chat:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = user_detail('shubham', 'Mr.', 23, 4.5)

friend_one = user_detail('sumit', 'Mr.', 4.2, 27)
friend_two = user_detail('amit', 'Mr.', 4.3, 26)
friend_three = user_detail('vipul','mr.', 4.1, 37)


friends_detail = [friend_one, friend_two, friend_three]


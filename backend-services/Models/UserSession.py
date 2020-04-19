class UserSession:

    def __init__(self, user_id, first_name, last_name, gender, profession, topic, focus_score, transcribed_at, transcribed_speech):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.profession = profession
        self.topic = topic
        self.focus_score = focus_score
        self.transcribed_at = transcribed_at
        self.transcribed_speech = transcribed_speech

    def to_dict(self):
        return {
            "user_id" : self.user_id,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "gender" : self.gender,
            "profession" : self.profession,
            "topic" :self.pic,
            "focus_score" : self.focus_score,
            "transcribed_at" : self.transcribed_at,
            "transcribed_speech" : self.transcribed_speech
        }
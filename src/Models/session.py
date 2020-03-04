class Session:
    def __init__(self, user_id,first_received_at,focus_score,transcribed_at,transcribed_speech):
        self.user_id = user_id
        self.first_received_at = first_received_at
        self.focus_score = focus_score
        self.transcribed_at = transcribed_at
        self.transcribed_speech = transcribed_speech
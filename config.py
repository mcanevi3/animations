class config:
    __conf = {
    "user_character_folder": "Free Knight 120x80/",
    "enemy_character_folder": "Huntress 150x150/"
    }
    @staticmethod
    def config(name):
        return config.__conf[name]

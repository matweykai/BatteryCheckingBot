class BotSettings:
    """This class encapsulates all data and logic for working with bot settings

    Attributes
    ----------
    phrases : list
        Phrases that bot tell when battery is low
    notification_name : str
        Name of notification that user will see
    battery_limit : int
        Threshold of tuning on notifications (battery_percents =< battery_limit -> turn on notifications)
    pause_time : int
        Number of seconds that bot sleeps between checking battery value
    showing_time : int
        During this time user will see notification
    icon_path : str
        Path to the image that you can see near notification, it should be .ico format
    """

    def __init__(self):
        self.__phrases = ["Battery charge is running out"]
        self.__notification_name = "Battery notification"
        self.__battery_limit = 100
        self.__pause_time = 5
        self.__showing_time = 3
        self.__icon_path = ""

    @property
    def phrases(self) -> list:
        return self.__phrases

    @property
    def notification_name(self) -> str:
        return self.__notification_name

    @property
    def battery_limit(self) -> int:
        return self.__battery_limit

    @property
    def pause_time(self) -> int:
        return self.__pause_time

    @property
    def showing_time(self) -> int:
        return self.__showing_time

    @property
    def icon_path(self) -> str:
        return self.__icon_path

    @phrases.setter
    def phrases(self, phrases_lst: list):
        if phrases_lst is None:
            raise AttributeError("Phrases list can't be None")
        self.__phrases = phrases_lst

    @notification_name.setter
    def notification_name(self, notif_name: str):
        if notif_name is None:
            raise AttributeError("Notification name can't be None")
        self.__notification_name = notif_name

    @battery_limit.setter
    def battery_limit(self, bat_limit: int):
        if bat_limit <= 0 or bat_limit >= 100:
            raise AttributeError("Wrong value of battery limit! Bounds: (0; 100)")
        self.__battery_limit = bat_limit

    @pause_time.setter
    def pause_time(self, p_time: int):
        if p_time <= 0:
            raise AttributeError("Pause time should be positive value")
        self.__pause_time = p_time

    @showing_time.setter
    def showing_time(self, duration: int):
        if duration <= 0 or duration > 10:
            raise AttributeError("Wrong duration value! Bounds: (0; 10]")
        self.__showing_time = duration

    @icon_path.setter
    def icon_path(self, i_path: str):
        if i_path is None:
            raise AttributeError("Icon path can't be None")
        if i_path[-4:] != '.ico':
            raise AttributeError("Wrong format of image! It should be .ico")

        self.__icon_path = i_path

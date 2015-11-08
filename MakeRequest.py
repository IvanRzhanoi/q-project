class MakeRequests(Rule):
    type = 'MAKE_REQUESTS_RULE'
    name = 'Make requests every 1 second'
    description = 'Make requests every 1 second'
    summary = 'Make requests every 1 second'

    devices = Output(field_type=None,
                    capabilities=[Capability.ON_OFF],
                    display_order=2,
                    description='Controlled device',
                    min_count=1)

    url = Value(field_type=Rule.FREE_TEXT,
                display_order=2,
                description='Url to be called',
                min_count=1, max_count=1,
                default='http://junction.esy.es/check.php')

    def __init__(self):
        super().__init__()
        self.__timer_id = None
        self.__timeout_ms = 300

    def start_my_timer(self):
        self.__timer_id = self.start_timer(self.__timeout_ms, self.__timer_id)
        # self.logger.info("Timer works")

    def cb(self, response):
        if response.code == 200:
            self.logger.info("Response: {0}".format(response.body))

            BrightnessCommand = DeviceCommand(self.devices[0])
            BrightnessCommand.state = LightState()

            if "1" in str(response.body):
                for d in self.devices:
                    self.send_command(DeviceOnCommand(d))
            elif "2" in str(response.body):
                for d in self.devices:
                    self.send_command(DeviceOffCommand(d))
            elif "3" in str(response.body):
                BrightnessCommand.state.brightness = 0.1
                for d in self.devices:
                    self.send_command(BrightnessCommand)
            elif "4" in str(response.body):
                BrightnessCommand.state.brightness = 1
                for d in self.devices:
                    self.send_command(BrightnessCommand)

            else:
                for d in self.devices:
                    self.send_command(DeviceOffCommand(d))

        else:
            self.logger.info("Server failed")
            self.logger.error("Failed: {0}".format(response))
        #command = DeviceCommand(lamp_id)
        #command.state = LightState()
        #self.logger.info(command.state)

        self.start_my_timer()

    def on_timeout(self, timer_id):
        self.make_request("GET", self.url[0].text, self.cb)

    def enable(self):
        super().enable()
        self.start_my_timer()
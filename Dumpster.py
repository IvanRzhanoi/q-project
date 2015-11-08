class HttpAndLog_NEW(Rule):
    type = 'HTTP_LOG_RULE_NEW'
    name = 'Http and log test rule_NEW'
    description = 'Test logging and http_NEW'
    summary = 'Test http and logging_NEW'

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

    url2 = Value(field_type=Rule.FREE_TEXT,
                display_order=2,
                description='Url to be called',
                min_count=1, max_count=1,
                default='http://junction.esy.es/list.php')

    def __init__(self):
        super().__init__()
        self.__timer_id = None
        self.__timeout_ms = 300

    def start_my_timer(self):
        self.__timer_id = self.start_timer(self.__timeout_ms, self.__timer_id)
        # self.logger.info("Timer works")

    def cb(self, response, data=None):
        if response.code == 200:
            self.logger.info("Response: {0}".format(response.body))
            '''
            self.logger.info("Error with settings")
            brightness = float(response.body.strip().split()[0])
            colourtemp = int(response.body.strip().split()[1])
            hue        = float(response.body.strip().split()[2])
            saturation = float(response.body.strip().split()[3])
            # self.logger.info("b='"+str(brightness)+"' colour='"+str(colourtemp)+"'")
            self.logger.info("Error with calling set_devices_brightness")
            self.set_devices_brightness(brightness,colourtemp, hue, saturation)
            self.logger.info("Error with command")
            BrightnessCommand = DeviceCommand(self.devices[0])
            BrightnessCommand.state = LightState()
            '''
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

    def set_devices_brightness(self, state, temperature, hue, saturation):
        # self.logger.info("set_devices_state")
        for d in self.devices:
            # self.logger.info("device: '" + d + "'")
            try:
                command = DeviceCommand(d)
                # self.logger.info("Getting state: '" + str(command.state) + "'")
                command.state = LightState()
                # self.logger.info("State: '" + str(command.state.brightness) + "'")
                command.state.brightness = state
                command.state.temperature = temperature

                command.state.colorMode = "hs"

                command.state.saturation = saturation
                command.state.hue = hue

                # self.logger.info("State set, state: '" + str(command.state.brightness) + "'")
                self.send_command(command)
            except:
                self.logger.error("Set brightness to")
            # self.logger.info("Set brightness to f")

        else:
            self.logger.error("Failed: {0}".format(response))
        self.logger.info("Error 0")
        #DeviceStateMessage()
        for d in self.devices:
            self.logger.info("Error 1")
            #status=self.send_command(DeviceStateMessage(d))
            self.logger.info("Error 2")
            #self.logger.info(status)
            self.logger.info("Error 3")
        #command = DeviceCommand(lamp_id)
        #command.state = LightState()
        #self.logger.info(command.state)
        data=self.logger.info(self.devices)
        self.make_request("POST", self.url2[0].text, data=data)
        self.start_my_timer()

    def on_timeout(self, timer_id):
        self.make_request("GET", self.url[0].text, self.cb)

    def enable(self):
        super().enable()
        self.start_my_timer()
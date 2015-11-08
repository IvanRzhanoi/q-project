class ChangeColor(Rule):
    type = 'Change_Color'
    name = "Change Color"
    description = 'Change Color'
    summary = 'Change Color'

    devices = Output(field_type=None,
                    capabilities=[Capability.ON_OFF],
                    display_order=2,
                    description='Controlled device',
                    min_count=1)

    def enable(self):
        super().enable()
        for d in self.devices:
            self.send_command(DeviceOffCommand(d))
            self.send_command(DeviceOnCommand(d))

        self.logger.info(self.devices[0])

        command = DeviceCommand(self.devices[0])
        command.state = LightState()
        command.state.colorMode = "hs"
        self.logger.info("Timestamp: {0}".format(get_timestamp()))
        self.logger.info("1 to 100: {0}".format(get_timestamp() % 100 + 1))
        command.state.hue = (get_timestamp() % 100 + 1) * 0.0628
        self.logger.info("hue: ".format(command.state.hue))
        command.state.saturation = 1

        self.send_command(command)
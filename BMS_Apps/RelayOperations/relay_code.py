class RelayKeys:

    def __init__(self):
        """initialize key codes"""
        self.HEADER = b'\xFF\xFF\xFF\xFF\x53\x4D\x41\x52\x54\x43\x4C\x4F\x55\x44\xAA\xAA'
        self.GET_STATUS = b'\x0b\x01\xFE\xFF\xFE\x00\x33\x01'
        self.OPERATION = b'\x0F\x01\xFE\xFF\xFE\x00\x31\x01'
        self.AC_PANEL_CONTROL = b'\x14\x01\xFE\xFF\xFE\xE0\xEE\x01'
        self.AC_PANEL_STATUS = b'\x0C\x01\xFE\xFF\xFE\xE0\xEC\x01'
        self.SCENE_CONTROL = b'\x0F\x01\xFE\xFF\xFE\x00\x02\x01'
        self.IR_OPERATION = b'\x0F\x01\xFE\xFF\xFE\xE0\x1C\x01'

        self.PANEL_MISC_PART = b'\x01\x17\x17\x17\x00'
        self.TRAIL = b'\x00\x00'

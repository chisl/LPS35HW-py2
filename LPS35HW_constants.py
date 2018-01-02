#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""LPS35HW: 260-1260 hPa absolute digital output barometer with water resistant package"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["STMicroelectronics"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

class REG:
	INTERRUPT_CFG = 11
	THS_P = 12
	WHO_AM_I = 15
	CTRL_REG1 = 16
	CTRL_REG2 = 17
	CTRL_REG3 = 18
	FIFO_CTRL = 20
	REF_P = 21
	RPDS = 24
	RES_CONF_1 = 26
	INT_SOURCE = 37
	FIFO_STATUS = 38
	STATUS = 39
	PRESS_OUT = 40
	TEMP_OUT = 43
	LPFP_RES = 51

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""LPS35HW: 260-1260 hPa absolute digital output barometer with water resistant package"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["STMicroelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from LPS35HW_constants import *

# name:        LPS35HW
# description: 260-1260 hPa absolute digital output barometer with water resistant package
# manuf:       STMicroelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/lps35hw.pdf
# date:        2018-01-04


# Derive from this class and implement read and write
class LPS35HW_Base:
	"""260-1260 hPa absolute digital output barometer with water resistant package"""
	# Register INTERRUPT_CFG
	# 8.1
	#       To generate an interrupt event based on a user defined threshold, DIFF_EN bit must be set
	#       to '1' and the threshold values stored in THS_P_L (0Ch) and THS_P_H (0Dh).
	#       When DIFF_EN = '1', PHE bit or PLE bit or both bits have to be enabled. PHE and PLE bits
	#       enable the interrupt generation on the positive or negative event respectively.
	#       When DIFF_EN is enabled and AUTOZERO or AUTORIFP is enabled, the defined
	#       pressure threshold values in THS_P (0Ch, 0Dh) is compared with:
	#       P_DIFF_IN=measured pressure - pressure reference
	#       The value of pressure reference is assigned depending on the AUTOZERO and
	#       AUTORIFP modes reported in the next two paragraphs.
	# 
	#       If AUTOZERO bit is set to '1', the measured pressure is used as reference on the register
	#       REF_P (15h, 16h and 17h). From now on, the output pressure registers PRESS_OUT
	#       (PRESS_OUT_H(2Ah), PRESS_OUT_L(29h) and PRESS_OUT_XL(28h)) are updated
	#       and the same value is also used for the interrupt generation: PRESS_OUT = measured
	#       pressure - REF_P
	#       After the first conversion AUTOZERO bit is automatically set to '0'. To return back to
	#       normal mode, RESET_AZ bit has to be set to '1'. This reset also the content of the REF_P
	#       registers. If AUTORIFP bit is set to '1', the measured pressure is used as reference on the
	#       register REF_P (15h, 16h and 17h). The output registers PRESS_OUT
	#       (PRESS_OUT_H(2Ah), PRESS_OUT_L(29h) and PRESS_OUT_XL(28h)) show the
	#       difference between the measured pressure and the content of the RPDS registers (18h and
	#       19h): PRESS_OUT = measured pressure - RPDS*256
	#       After the first conversion AUTORIFP bit is automatically set to '0'. To return back to normal
	#       mode, RESET_ARP bit has to be set to '1'. 
	
	
	def setINTERRUPT_CFG(self, val):
		"""Set register INTERRUPT_CFG"""
		self.write(REG.INTERRUPT_CFG, val, 8)
	
	def getINTERRUPT_CFG(self):
		"""Get register INTERRUPT_CFG"""
		return self.read(REG.INTERRUPT_CFG, 8)
	
	# Bits AUTORIFP
	# AutoRifP function enable. 
	# Bits RESET_ARP
	# Reset AutoRifP function. 
	# Bits AUTOZERO
	# Autozero enable. 
	# Bits RESET_AZ
	# Reset Autozero function. 
	# Bits DIFF_EN
	# Interrupt generation enable. 
	# Bits LIR
	# Latch interrupt request to the INT_SOURCE register. 
	# Bits PLE
	# Enable interrupt generation on differential pressure low event. 
	# Bits PHE
	# Enable interrupt generation on differential pressure high event. 
	# Register THS_P
	# 8.2-3 
	#         Threshold value for pressure interrupt generation.
	#         This register contains the threshold value for pressure interrupt generation. 
	
	
	def setTHS_P(self, val):
		"""Set register THS_P"""
		self.write(REG.THS_P, val, 16)
	
	def getTHS_P(self):
		"""Get register THS_P"""
		return self.read(REG.THS_P, 16)
	
	# Bits THS
	# Refer to Section 10.2: "THS_P_L (0Ch)" 
	# Register WHO_AM_I
	# 8.4
	#       Device Who am I 
	
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register CTRL_REG1
	# 8.5
	#       Control register 1
	#       When ODR bits are set to '000' the device is in Power down mode. When the device is in
	#       power-down mode, almost all internal blocks of the device are switched off to minimize
	#       power consumption. I2C interface is still active to allow communication with the device. The
	#       configuration registers content is preserved and output data registers are not updated,
	#       therefore keeping the last data sampled in memory before going into power- down mode.
	#       If ONE_SHOT bit in CTRL_REG2(11h) is set to '1', One-shot mode is triggered and a new
	#       acquisition starts when it is required. This enabling is effective only if the device was
	#       previously in power-down mode (ODR bits set to '000'). Once the acquisition is completed
	#       and the output registers updated, the device automatically enters in power down mode.
	#       ONE_SHOT bit self-clears itself.
	#       When ODR bits are set to a value different than '000', the device is in Continuous mode
	#       and automatically acquires a set of data (pressure and temperature) at the frequency
	#       selected through ODR[2,0] bits. 
	# 
	#       Once the additional low pass filter has been enable through the EN_LPFP bit, it is possible
	#       to configure the device bandwidth acting on LPFP_CFG bit. Refer to Table 20: "Low-pass
	#       filter configurations". 
	# 
	#       Table 20: Low-pass filter configurations
	#       EN_LPFP LPFP_CFG Additional low pass filter status    Device bandwidth
	#       0       x        Disabled                             ODR/2
	#       1       0        Enabled                              ODR/9
	#       1       1        Enabled                              ODR/20 
	# 
	#       The BDU bit is used to inhibit the update of the output registers between the reading of
	#       upper and lower register parts. In default mode (BDU = ‘0’), the lower and upper register
	#       parts are updated continuously. When the BDU is activated (BDU = ‘1’), the content of the
	#       output registers is not updated until PRESS_OUT_H is read, avoiding the reading of values
	#       related to different samples. 
	
	
	def setCTRL_REG1(self, val):
		"""Set register CTRL_REG1"""
		self.write(REG.CTRL_REG1, val, 8)
	
	def getCTRL_REG1(self):
		"""Get register CTRL_REG1"""
		return self.read(REG.CTRL_REG1, 8)
	
	# Bits unused_0
	# This bit must be set to ‘0’ for proper operation of the device 
	# Bits ODR
	# Output data rate selection. 
	# Bits EN_LPFP
	# Enable low-pass filter on pressure data. 
	# Bits LPFP_CFG
	# Low-pass configuration register. 
	#           Refer to Table 20: "Low- pass filter configurations". 
	
	# Bits BDU
	# Block data update.
	#           To guarantee the correct behavior of BDU feature, th PRESS_OUT_H (2Ah) must be the last address read. 
	
	# Bits SIM
	# SPI Serial Interface Mode selection. 
	# Register CTRL_REG2
	# 8.6
	#       Control register 2 
	
	
	def setCTRL_REG2(self, val):
		"""Set register CTRL_REG2"""
		self.write(REG.CTRL_REG2, val, 8)
	
	def getCTRL_REG2(self):
		"""Get register CTRL_REG2"""
		return self.read(REG.CTRL_REG2, 8)
	
	# Bits BOOT
	# Reboot memory content. 
	#           The bit is self-cleared when the BOOT is completed. 
	#           The BOOT bit is used to refresh the content of the internal registers stored in the Flash
	#           memory block. At device power-up the content of the Flash memory block is transferred to
	#           the internal registers related to the trimming functions to allow correct behavior of the
	#           device itself. If for any reason the content of the trimming registers is modified, it is
	#           sufficient to use this bit to restore the correct values. When the BOOT bit is set to ‘1’, the
	#           content of the internal Flash is copied inside the corresponding internal registers and is
	#           used to calibrate the device. These values are factory trimmed and they are different for 
	#           every device. They allow correct behavior of the device and normally they should not be
	#           changed. At the end of the boot process the BOOT bit is set again to ‘0’ by hardware. The
	#           BOOT bit takes effect after one ODR clock cycle. 
	
	# Bits FIFO_EN
	# FIFO enable. 
	# Bits STOP_ON_FTH
	# Stop on FIFO threshold. Enable FIFO watermark level use. 
	# Bits IF_ADD_INC
	# Register address automatically incremented during a multiple byte access with a
	#           serial interface (I2C or SPI). 
	
	# Bits I2C_DIS
	# Disable I2C interface. 
	# Bits SWRESET
	# Software reset. 
	#           The bit is self-cleared when the reset is completed. 
	#           SWRESET is the software reset bit. The following device registers (INTERRUPT_CFG,
	#           THS_P_L, THS_P_H, CTRL_REG1, CTRL_REG2, CTRL_REG3, FIFO_CTRL,
	#           RIF_P_XL,RIF_P_L,RIF_P_H) are reset to the default value if the SWRESET bit is set to
	#           '1'. SWRESET bit comes back to '0' by hardware. 
	
	# Bits unused_0
	# This bit must be set to ‘0’ for proper operation of the device. 
	# Bits ONE_SHOT
	# One-shot enable. 
	#           The ONE_SHOT bit is used to start a new conversion when the ODR[2,0] bits in
	#           CTRL_REG1(10h)are set to ‘000’. Writing a ‘1’ in ONE_SHOT triggers a single
	#           measurement of pressure and temperature. Once the measurement is done, the
	#           ONE_SHOT bit will self-clear, the new data are available in the output registers, and the
	#           STATUS_REG bits are updated. 
	
	# Register CTRL_REG3
	# 8.7
	#       Control register 3 - INT_DRDY pin control register 
	
	
	def setCTRL_REG3(self, val):
		"""Set register CTRL_REG3"""
		self.write(REG.CTRL_REG3, val, 8)
	
	def getCTRL_REG3(self):
		"""Get register CTRL_REG3"""
		return self.read(REG.CTRL_REG3, 8)
	
	# Bits INT_H_L
	# Interrupt active-high/low. 
	# Bits PP_OD
	# Push-pull/open drain selection on interrupt pads. 
	# Bits F_FSS5
	# FIFO full flag on INT_DRDY pin. 
	# Bits F_FTH
	# FIFO threshold (Watermark) status on INT_DRDY pin. 
	# Bits F_OVR
	# FIFO overrun interrupt on INT_DRDY pin. 
	# Bits DRDY
	# Data-ready signal on INT_DRDY pin. 
	# Bits INT_S
	# Data signal on INT_DRDY pin control bits. 
	# Register FIFO_CTRL
	# 8.8
	#       FIFO control register 
	
	
	def setFIFO_CTRL(self, val):
		"""Set register FIFO_CTRL"""
		self.write(REG.FIFO_CTRL, val, 8)
	
	def getFIFO_CTRL(self):
		"""Get register FIFO_CTRL"""
		return self.read(REG.FIFO_CTRL, 8)
	
	# Bits F_MODE
	# FIFO mode selection. 
	# Bits WTM
	# FIFO watermark level selection. 
	# Register REF_P
	# 8.9
	#       Reference pressure
	#       The value is expressed as 2’s complement.
	#       The reference pressure value is used when AUTOZERO or AUTORIFP function is
	#       enabled(refer to the Section 10.7: "CTRL_REG3 (12h)" register) and for the Autozero
	#       function (refer to the Section 10.1: "INTERRUPT_CFG (0Bh)" register). 
	
	
	def setREF_P(self, val):
		"""Set register REF_P"""
		self.write(REG.REF_P, val, 24)
	
	def getREF_P(self):
		"""Get register REF_P"""
		return self.read(REG.REF_P, 24)
	
	# Bits REFL
	# This register contains the low part of the reference pressure value. 
	#           The Reference pressure value is a 24-bit data and it is composed of Section 10.11:
	#           "REF_P_H_17h", Section 10.10: "REF_P_L_16h" and Section 10.9: "REF_P_XL (15h)". 
	
	# Register RPDS
	# 8.12
	#       Pressure offset
	#       If, after the soldering of the component, a residual offset is still present, it can be removed
	#       with a one-point calibration.
	#       After the soldering, the measured offset can be stored in the Section 10.13:
	#       "RPDS_H_19h" and Section 10.12: "RPDS_L_18h" registers and automatically subtracted
	#       from the pressure output registers: the output pressure register PRESS_OUT (28h, 29h
	#       and 2Ah) is provided as the difference between the measured pressure and the content of
	#       the register 256*RPDS (18h, 19h)*.
	#       *DIFF_EN = '0', AUTOZERO = '0', AUTORIFP = '0' 
	
	
	def setRPDS(self, val):
		"""Set register RPDS"""
		self.write(REG.RPDS, val, 16)
	
	def getRPDS(self):
		"""Get register RPDS"""
		return self.read(REG.RPDS, 16)
	
	# Bits RPDS
	# Register RES_CONF_1
	# 8.14
	#       Low-power mode configuration 
	
	
	def setRES_CONF_1(self, val):
		"""Set register RES_CONF_1"""
		self.write(REG.RES_CONF_1, val, 8)
	
	def getRES_CONF_1(self):
		"""Get register RES_CONF_1"""
		return self.read(REG.RES_CONF_1, 8)
	
	# Bits unused_0
	# These bits must be set to ‘0’ for proper operation of the device. 
	# Bits reserved_1
	# The content of this bit must not be modified for proper operation of the device 
	# Bits LC_EN
	# Low current mode enable. 
	#           The LC_EN bit must be changed only with the device in power down and not during operation. Once LC_EN bit
	#           is configured, it affects both One-shot mode and Continuous mode. 
	
	# Register INT_SOURCE
	# 8.15
	#       Interrupt source 
	
	
	def setINT_SOURCE(self, val):
		"""Set register INT_SOURCE"""
		self.write(REG.INT_SOURCE, val, 8)
	
	def getINT_SOURCE(self):
		"""Get register INT_SOURCE"""
		return self.read(REG.INT_SOURCE, 8)
	
	# Bits BOOT_STATUS
	# If ‘1’ indicates that the Boot (Reboot) phase is running. 
	# Bits unused_0
	# These bits must be set to ‘0’ for proper operation of the device. 
	# Bits IA
	# Interrupt active. 
	# Bits PL
	# Differential pressure Low. 
	# Bits PH
	# Differential pressure High. 
	# Register FIFO_STATUS
	# 8.16
	#       FIFO status 
	#       Note: When the number of unread samples in FIFO is greater than the threshold level set in
	#             register Section 10.8: "FIFO_CTRL (14h)", FTH value is ‘1’. 
	
	
	def setFIFO_STATUS(self, val):
		"""Set register FIFO_STATUS"""
		self.write(REG.FIFO_STATUS, val, 8)
	
	def getFIFO_STATUS(self):
		"""Get register FIFO_STATUS"""
		return self.read(REG.FIFO_STATUS, 8)
	
	# Bits FTH_FIFO
	# FIFO threshold status. 
	# Bits OVR
	# FIFO overrun status. 
	# Bits FSS
	# FIFO stored data level. 
	#           6'b000000: FIFO is empty , 6'b100000: FIFO is full and has 32 unread samples. 
	# 
	#           Table 33: FIFO_STATUS example: OVR/FSS details
	#           FTH  OVRN FSS     Description
	#           0    0    000000  FIFO empty
	#           1    0    000001  1 unread sample
	#           ...
	#           1    0    100000  32 unread sample 
	#         
	
	# Register STATUS
	# 8.17
	#       Status register. This register is updated every ODR cycle. 
	
	
	def setSTATUS(self, val):
		"""Set register STATUS"""
		self.write(REG.STATUS, val, 8)
	
	def getSTATUS(self):
		"""Get register STATUS"""
		return self.read(REG.STATUS, 8)
	
	# Bits unused_0
	# Bits T_OR
	# Temperature data overrun. 
	# Bits P_OR
	# Pressure data overrun. 
	# Bits unused_1
	# Bits T_DA
	# Temperature data available. 
	# Bits P_DA
	# Pressure data available. 
	# Register PRESS_OUT
	# 8.18-20
	#       The pressure output value is a 24-bit data that contains the measured pressure. It is
	#       composed of Section 10.20: "PRESS_OUT_H_2Ah", Section 10.19: "PRESS_OUT_L_29h"
	#       and Section 10.18: "PRESS_OUT_XL_28h" . The value is expressed as 2’s complement.
	#       The output pressure register PRESS_OUT is provided as the difference between the
	#       measured pressure and the content of the register RPDS (18h, 19h) 
	#       (DIFF_EN = '0', AUTOZERO = '0', AUTORIFP = '0'). 
	#       Please refer to section Section 5.4: "How to interpret pressure readings" for additional info. 
	
	
	def setPRESS_OUT(self, val):
		"""Set register PRESS_OUT"""
		self.write(REG.PRESS_OUT, val, 24)
	
	def getPRESS_OUT(self):
		"""Get register PRESS_OUT"""
		return self.read(REG.PRESS_OUT, 24)
	
	# Bits PRESS_OUT
	# Register TEMP_OUT
	# 8.21-23
	#       Temperature output value
	#       The temperature output value is a 24-bit data that contains the measured temperature. It is
	#       composed of Section 10.20: "PRESS_OUT_H_2Ah", and Section 10.18:
	#       "PRESS_OUT_XL_28h". The value is expressed as 2’s complement. 
	
	
	def setTEMP_OUT(self, val):
		"""Set register TEMP_OUT"""
		self.write(REG.TEMP_OUT, val, 24)
	
	def getTEMP_OUT(self):
		"""Get register TEMP_OUT"""
		return self.read(REG.TEMP_OUT, 24)
	
	# Bits TEMP_OUT
	# Register LPFP_RES
	# 8.23 
	#       Low-pass filter reset register.
	#       If the LPFP is active, in order to avoid the transitory phase, the filter can be reset by
	#       reading this register before getting out pressure measurements. 
	
	
	def setLPFP_RES(self, val):
		"""Set register LPFP_RES"""
		self.write(REG.LPFP_RES, val, 8)
	
	def getLPFP_RES(self):
		"""Get register LPFP_RES"""
		return self.read(REG.LPFP_RES, 8)
	
	# Bits LPFP_RES

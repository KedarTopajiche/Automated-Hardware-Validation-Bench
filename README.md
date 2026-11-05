# Automated Hardware-in-the-Loop (HIL) Validation Bench

An automated embedded testing and telemetry validation fixture developed on an ESP8266 microcontroller and Python host environment. This bench evaluates Time-of-Flight (ToF) laser ranging over I2C, captures edge-triggered hardware interrupt service routines (ISRs), and streams automated PASS/FAIL regression assertions to a host CSV log.

---

## System Architecture

```text
+------------------------+             +------------------------+
| STMicroelectronics     |   I2C Bus   | ESP8266 NodeMCU        |
| VL53L0X ToF Sensor     |<----------->| (GPIO4/D2 SDA,         |
| Address: 0x29 (50 kHz) |             |  GPIO5/D1 SCL)         |
+------------------------+             +-----------+------------+
                                                   |
+------------------------+     GPIO12/D6           |
| External Input / Touch |-------------------------+
| Active-Low Trigger     | (Hardware ISR / FALLING)
+------------------------+
                                                   |
                                                   | UART Serial
                                                   | (115200 Baud)
                                                   v
                                       +------------------------+
                                       | Host Test Automation   |
                                       | Python (PySerial)      |
                                       | CSV Telemetry Logger   |
                                       +------------------------+

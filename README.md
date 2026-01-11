# SM85CL RS-485 Servo Control using Python + RS485/TTL Converter + ESP32/Arduino

This repository demonstrates how to control the **Feetech SM85CL** RS-485 robotic servo using Python and a standard **TTL ↔ RS485 converter**, along with ESP32 or Arduino as the serial interface.

The project includes:
- Python control scripts
- Servo scanning utilities (ID discovery)
- Fast motion control (0° ↔ 180°)
- Screen/fingertip mapping control
- Wiring diagrams and setup instructions
- Feetech SDK integration
- Troubleshooting + notes

---

## 🚀 Features

- Full RS-485 control (SMS1.0 protocol)
- Ultra-fast low-latency commands
- Supports multi-servo bus chaining
- Fingertip/mouse screen control
- Python FTServo SDK integration
- Works with ESP32, Arduino Uno/Mega, PC, Linux

---

## 🔧 Hardware Required

| Component | Purpose |
|---|---|
| Feetech **SM85CL** Servo | RS-485 robotic actuator |
| **TTL ↔ RS485 Converter** | Signal level conversion |
| ESP32 / Arduino / USB-UART | Serial host |
| 7.4–8.4V Li-ion / LiPo | Servo power |
| USB cable | PC ↔ host communication |
| Common GND | Bus reference |

---

## 🧠 What is RS-485?

**RS-485** is a balanced differential industrial communication protocol used for:
- Long distance data
- Low noise robotics environments
- Multi-device bus networks

Compared to hobby PWM servos:
| Protocol | Wires | Feedback | Multi-Servo | Latency | Use-Case |
|---|---|---|---|---|---|
| PWM | 3 | ❌ No | ❌ No | High | Hobby |
| RS-485 | 4 | ✔ Yes | ✔ Yes | Low | Robotics / AGVs |

SM85CL fully supports:
- Position feedback
- Torque feedback
- Velocity mode
- Multi-turn mode
- PID tuning

---

## 📂 Project Structure


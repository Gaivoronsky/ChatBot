from core.core import ManagementTG


if __name__ == '__main__':
    tg = ManagementTG()
    tg.loop()
    tg.client.disconnect()

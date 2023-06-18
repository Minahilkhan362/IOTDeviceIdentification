from joblib import load
import os
from sklearn.preprocessing import normalize


class DeviceVerificationService:
    def __init__(self):
        self._pred_label_mapper = {'Amazon Echo': 0, 'Aria': 1, 'August Doorbell Cam': 2, 'Awair air quality monitor': 3, 'Belkin Camera': 4, 'Belkin Wemo switch': 5, 'Belkin wemo motion sensor': 6, 'Blipcare Blood Pressure meter': 7, 'Canary Camera': 8, 'D-LinkCam': 9, 'D-LinkDayCam': 10, 'D-LinkDoorSensor': 11, 'D-LinkHomeHub': 12, 'D-LinkSensor': 13, 'D-LinkSiren': 14, 'D-LinkSwitch': 15, 'D-LinkWaterSensor': 16, 'Dropcam': 17, 'EdimaxCam': 18, 'EdimaxPlug1101W': 19, 'EdimaxPlug2101W': 20, 'EdnetCam': 21, 'EdnetGateway': 22, 'Google Chromecast': 23, 'HP Printer': 24, 'Hello Barbie': 25, 'HomeMaticPlug': 26, 'HueBridge': 27, 'HueSwitch': 28, 'IKettle2': 29, 'Insteon Camera': 30, 'Light Bulbs LiFX Smart Bulb': 31,
                                   'Lightify': 32, 'MAXGateway': 33, 'NEST Protect smoke alarm': 34, 'Nest Dropcam': 35, 'Netatmo Welcome': 36, 'Netatmo weather station': 37, 'Non-IoT': 38, 'PIX-STAR Photo-frame': 39, 'Phillip Hue Lightbulb': 40, 'Ring Door Bell': 41, 'Samsung SmartCam': 42, 'Smart Things': 43, 'SmarterCoffee': 44, 'TP-Link Day Night Cloud camera': 45, 'TP-Link Smart plug': 46, 'TP-LinkPlugHS100': 47, 'TP-LinkPlugHS110': 48, 'TPLink Router Bridge LAN (Gateway)': 49, 'Triby Speaker': 50, 'WeMoInsightSwitch': 51, 'WeMoLink': 52, 'WeMoSwitch': 53, 'Withings': 54, 'Withings Aura smart sleep sensor': 55, 'Withings Smart Baby Monitor': 56, 'Withings Smart scale': 57, 'iHome': 58, 'unknown maybe cam': 59}

    def predict_device_name(self, request):
        features = self._get_features(request)
        features = normalize(features)
        y_pred = self. _predict(features)
        return self._get_label(y_pred)

    def _get_features(self, request):
        # feature_from_request = [[request.META['CONTENT_LENGTH'], request.META['Ether_type'],
        #                         request.META['LLC_ctrl'], request.META['EAPOL_version'],
        #                         request.META['EAPOL_type'], request.META['IP_ihl'],
        #                         request.META['IP_tos'], request.META['IP_len'],
        #                         request.META['IP_flags'], request.META['IP_DF'],
        #                         request.META['IP_ttl'], request.META['IP_options'],
        #                         request.META['ICMP_code'], request.META['TCP_dataofs'],
        #                         request.META['TCP_FIN'], request.META['TCP_ACK'],
        #                         request.META['TCP_window'], request.META['UDP_len'],
        #                         request.META['DHCP_options'], request.META['BOOTP_hlen'],
        #                         request.META['BOOTP_flags'], request.META['BOOTP_sname'],
        #                         request.META['BOOTP_file'], request.META['BOOTP_options'],
        #                         request.META['DNS_qr'], request.META['DNS_rd'],
        #                         request.META['DNS_qdcount'], request.META['dport_class'],
        #                         request.META['payload_bytes'], request.META['entropy']]]

        test_data = [[69, 2048, 0, 0, 0, 5, 0, 69, 2, 0, 64, 0, 0, 5, 0, 1,
                     9660, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 5, 29, 4.1852301329094015]]

        return test_data

    def _predict(self, features):
        path = os.getcwd() + '/iot_app/services/'
        model = load(path + 'Model.joblib')
        return model.predict(features)

    def _get_label(self, y_pred):
        for key in self._pred_label_mapper .keys():
            if self._pred_label_mapper[key] == y_pred:
                return key

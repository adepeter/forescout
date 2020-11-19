from python_arptable import get_arp_table

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


arp_table_data = get_arp_table()


class ARPListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        new_arp_table_data = []
        if arp_table_data:
            arp_data = {}
            for i, v in enumerate(arp_table_data):
                for k in v:
                    arp_data['ip_address'] = v['IP address']
                    arp_data['mac_address'] = v['HW address']
                    arp_data['device_name'] = v['Device']
                new_arp_table_data.append(arp_data)
        return Response(new_arp_table_data, status=status.HTTP_200_OK)

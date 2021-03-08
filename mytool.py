class GetIps:
    def __init__(self, txt):
        self.txt = txt
        self.my_ips = self.txt.split('<li id="l')
        self.all_vpc = []
        self.all_npc = []
        self.ip_100mb = []
        self.ip_250mb = []
        self.ip_500mb = []
        self.ip_1gb = []
        self.relatorio = []

    def get_all_vpc(self):
        for vpc in self.my_ips:
            print(vpc)
            if 'VPC' in vpc:
                get_vpc = vpc.split('<span id="ip">')[1].split('</span>')[0]
                print(get_vpc)
                self.all_vpc.append(get_vpc)

            return self.all_vpc

    def get_all_npc(self):
        for ip in self.my_ips:
            if 'NPC' in ip:
                get_npc = ip.split('<span id="ip">')[1].split('</span>')[0]
                self.all_npc.append(get_npc)
        return self.all_npc

    def get_ip_100mb(self):
        for ip in self.my_ips:
            if '100 Mbit' in ip:
                get_ip_100mb = ip.split('<span id="ip">')[1].split('</span>')[0]
                self.ip_100mb.append(get_ip_100mb)
        if len(self.ip_100mb) == 0:
            return '0'
        else:
            return self.ip_100mb

    def get_ip_250mb(self):
        for ip in self.my_ips:
            if '250 Mbit' in ip:
                get_ip_250mb = ip.split('<span id="ip">')[1].split('</span>')[0]
                self.ip_250mb.append(get_ip_250mb)
        if len(self.ip_250mb) == 0:
            return '0'
        else:
            return self.ip_250mb

    def get_ip_500mb(self):
        for ip in self.my_ips:
            if '500 Mbit' in ip:
                get_ip_500mb = ip.split('<span id="ip">')[1].split('</span>')[0]
                self.ip_500mb.append(get_ip_500mb)
        if len(self.ip_500mb) == 0:
            return '0'
        else:
            return self.ip_500mb

    # 1 Gbit

    def get_ip_1gb(self):
        for ip in self.my_ips:
            if '1 Gbit/s' in ip:
                get_ip_1gb = ip.split('<span id="ip">')[1].split('</span>')[0]
                self.ip_1gb.append(get_ip_1gb)
        if len(self.ip_1gb) == 0:
            return '0'
        else:
            return self.ip_1gb

    def get_relatorio(self):

        self.relatorio.append(len(self.all_npc))
        self.relatorio.append(len(self.all_vpc))
        self.relatorio.append(len(self.ip_100mb))
        self.relatorio.append(len(self.ip_250mb))
        self.relatorio.append(len(self.ip_500mb))
        self.relatorio.append(len(self.ip_1gb))
        return self.relatorio

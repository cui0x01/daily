a,A=manager_act_ip='ipconfig static manage ','192.168.11.1 255.255.255.0'
b,B=manager_sby_ip='ipconfig static manage-standby ','192.168.11.2 255.255.255.0'
c,C=service_act_ip='ipconfig static service ','192.168.12.1 255.255.255.0'
d,D=service_sby_ip='ipconfig static service-stan','dby 192.168.12.2 255.255.255.0'
e,E=manager_vlan_id='ipconfig vlanid ','manage 100'
f,F=manager_vlan_cos='ipconfig vlanoption ','manage tag 4'
g,G=service_vlan_id='ipconfig vlanid ','service 200'
h,H=service_vlan_cos='ipconfig vlanoption ','service tag 4'
i,I=route_del1='route del ','0.0.0.0'
j,J=route_del2='route del ','10.8.3.56'
k,K=route_del3='route del ','10.8.3.147'
l,L=route_del4='route del ','10.8.3.0'
m,M=route_add='route add 0.0.0.0 ','0.0.0.0 192.168.11.254'

p = [b,d,g,h,a,c,e,f,i,j,k,l,m]
q = [B,D,G,H,A,C,E,F,I,J,K,L,M]
group = zip(p,q)
for p,q in group:
    crt.Screen.Send(p)
    crt.Sleep(1000)
    crt.Screen.Send(q+'\n')
    crt.Sleep(3000)




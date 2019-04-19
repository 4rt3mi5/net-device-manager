from device.models import DeviceType

def init_typemodel():
    DEVICE_TYPE = (
        '华为-S5700S-52P-LI-AC', '华为-S5700-24TP-PWR-SI',
        '华为-AR3260E-S-Router', '华为-S5720-56C-EI-AC',
        '华为-S5720-28X-PWR-SI-AC', '华为-AR2220E-S-Router',
        '华为-USG6530-Firewall'
    )
    for t in DEVICE_TYPE:
        DeviceType.objects.create(name=t)
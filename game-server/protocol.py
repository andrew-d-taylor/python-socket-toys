__author__ = 'andrew'


def loginSuccess(mapx, mapy):
    return "200 " + mapx + " " + mapy + "\n"


def playerMessage(playerId, messageText):
    return "100 " + playerId + " " + messageText + "\n"


def playerWon(playerId):
    return "101 " + playerId + " won the game!\n"


def mapSubsection(x1, y1, x2, y2, tileNumber):
    return "102 " + x1 + " " + y1 + " " + x2 + " " + y2 + " " + tileNumber + " \n"


def cookieThrown(cookieId, cookieX, cookieY, dir):
    return "103 " + cookieId + " " + cookieX + " " + cookieY + " " + dir + "\n"


def playerCookieUpdate(playerId, playerX, playerY, cookieCount):
    return "104 " + playerId + " " + playerX + " " + playerY + " " + cookieCount + "\n"


def badCommand(message):
    return "400 " + message + "\n"


def serverError(message):
    return "500 " + message + "\n"


class ClientRequest():
    def __init__(self, requestString):
        requestSplit = requestString.split()
        self.command = Command(requestSplit[0])
        if self.command.isLogin():
            self.playerId = requestSplit[1]
        elif self.command.isMessage():
            self.playerId = requestSplit[1]
            self.message = requestSplit[2]
        else:
            self.direction = Direction(requestSplit[1])


class Command():
    def __init__(self, requestSubstring):
        self.__command = self.__parseCommand(requestSubstring)

    def __parseCommand(self, requestSubstring):
        requestSubstring = requestSubstring.lower()
        if requestSubstring == "login" or requestSubstring == "l":
            return "login"
        elif requestSubstring == "move" or requestSubstring == "m":
            return "move"
        elif requestSubstring == "throw" or requestSubstring == "t":
            return "throw"
        elif requestSubstring == "msg":
            return "msg"
        else:
            raise RequestParsingException

    def isLogin(self):
        return self.__command == "login"

    def isMove(self):
        return self.__command == "move"

    def isThrow(self):
        return self.__command == "throw"

    def isMessage(self):
        return self.__command == "msg"


class Direction():
    def __init__(self, requestSubstring):
        self.__direction = self.__parseDirection(requestSubstring)

    def __parseDirection(self, requestSubstring):
        requestSubstring = requestSubstring.lower()
        if requestSubstring == "up" or requestSubstring == "u":
            return "up"
        elif requestSubstring == "down" or requestSubstring == "d":
            return "down"
        elif requestSubstring == "left" or requestSubstring == "l":
            return "left"
        elif requestSubstring == "right" or requestSubstring == "r":
            return "right"
        else:
            raise RequestParsingException

    def isUp(self):
        return self.__direction == "up"

    def isDown(self):
        return self.__direction == "down"

    def isLeft(self):
        return self.__direction == "left"

    def isRight(self):
        return self.__direction == "right"


class RequestParsingException(Exception):
    pass
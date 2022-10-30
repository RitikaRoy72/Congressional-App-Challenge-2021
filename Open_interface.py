import pygame
import pandas as pd



class Open_window:
  """Open a window to run this app"""
  
  def __init__():
    """Initilize the window"""
    pygame.init()
    
    
  def run_the_app_murder_graph():
    """Start the window to open the app"""
    pygame.init()
    #Give parameters for the screen dimensions, and font type
    length = 10000
    width = 450
    #Name the colors that will be used
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    #Open and name the window
    screen = pygame.display.set_mode((length, width))
    pygame.display.set_caption("Crime Rates")

    #Open the image
    murder = pygame.image.load(r'Murder.png')
    murder = pygame.transform.scale(murder, (600, 400))

    #Print data next to the graph
    data = pd.read_csv('US_violent_crime.csv')
    font = pygame.font.Font('freesansbold.ttf', 10)
    
    #Pygame is not compatible with a loop input of data: this process had to be done manually
    data = data.iloc[:, 0:2]
    text = font.render(str(data), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (730 , 10)
    
    #Create a restart button
    
    

    active = False
    #Execute all of these functions
    while True:
      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          text = "Click here to restart"
          box = font.render(str(text), True, green, blue)
          boxRect = box.get_rect()
          boxRect.center = (500 , 10)
          screen.blit(box, boxRect) 
          if boxRect.collidepoint(event.pos):
            active = True
            import main
            print(main.interface.open())
          else:
            active = False
            break
      
      #Set the background color
      screen.fill(red)

      #Output the image
      screen.blit(murder, (0, 0))

      #Get the rectangle to print text for every state
      screen.blit(text, textRect)

      #OUtput restart box
      
      
      #Detect the use events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
          quit()
      #Make this screen available
      pygame.display.update()


  def run_the_app_assault_graph():
    """Start the window to open the app"""
    pygame.init()
    #Give parameters for the screen dimensions
    length = 800
    width = 450
    #Name the colors that will be used
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    
    #Open and name the window
    screen = pygame.display.set_mode((length, width))
    pygame.display.set_caption("Crime Rates")
    
    #Open the image
    Assault = pygame.image.load(r'Assault.png')
    Assault = pygame.transform.scale(Assault, (600, 400))

    #Print data next to the graph
    data = pd.read_csv('US_violent_crime.csv')
    font = pygame.font.Font('freesansbold.ttf', 10)
    #Start this process
    data = data.iloc[1, [0,2]]
    text = font.render(str(data), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (730 , 10)

    #Execute this data
    while True:
      #Set the background color
      screen.fill(red)
      #Output the image
      screen.blit(Assault, (0, 0))
      #Print a rectangle
      screen.blit(text, textRect)
      #Detect the use events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
          quit()
      #Make this screen available
      pygame.display.update()


  def run_the_app_sexual_assault_graph():
    """Start the window to open the app"""
    pygame.init()
    #Give parameters for the screen dimensions
    length = 800
    width = 450
    #Name the colors that will be used
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    #Open and name the window
    screen = pygame.display.set_mode((length, width))
    pygame.display.set_caption("Crime Rates")

    #Open the image
    sex_assault = pygame.image.load(r'SexualAssaultData.png')
    sex_assault = pygame.transform.scale(sex_assault, (600, 400))

    #Print data next to the graph
    data = pd.read_csv('US_violent_crime.csv')
    data = data.iloc[0:50, [0,4]]
    font = pygame.font.Font('freesansbold.ttf', 10)
    text = font.render(str(data), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (730 , 10)

    #Execute this process
    while True:
      #Set the background color
      screen.fill(red)
      #Output the image
      screen.blit(sex_assault, (0, 0))
      #Print a rectangle
      screen.blit(text, textRect)
      #Detect the use events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
          quit()
      #Make this screen available
      pygame.display.update()


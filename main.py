# import sys module
import pygame
import print_graphs_whole_country
import Open_interface
import Give_data_info
import os
#import sys

class start():
  """A class to start up the entire app"""

  def functions():
    while True:
      while True:
        print("Type in 'quit' to end this program")
        ask = input("What would you like? (state list, crime list, Alabama(code needs fixing), murder, assault, sexual assault) \n")
        acceptableList = ["state list","crime list","alabama","murder","assault","sexual assault", "quit"]
        if ask in acceptableList:
          print("\n\n")
          break
        else:
          print("This is unacceptable! Please choose one of the existing options.\n\n")
          

      if ask == 'state list':
        print(Give_data_info.data_type.print_state_names())
        input("Type enter to return to the main menu")
        os.system("clear")

      elif ask == 'crime list':
        print(Give_data_info.data_type.print_crime_types())
        input("Type enter to return to the main menu")
        os.system("clear")
      

      elif ask == 'murder':
        print_graphs_whole_country.plot_stats_country.print_stats_for_murder()
        print(Open_interface.Open_window.run_the_app_murder_graph())
          

      elif ask == 'assault':
        print_graphs_whole_country.plot_stats_country.print_stats_for_state_assault()
        print(Open_interface.Open_window.run_the_app_assault_graph())
          

      elif ask == 'sexual assault':
        print_graphs_whole_country.plot_stats_country.print_stats_state_sexual_assault()
        print(Open_interface.Open_window.run_the_app_sexual_assault_graph())
        

      elif ask =='quit':
        print("Thanks for using this program!")
        break

  def open():
    # pygame.init() will initialize all
    pygame.init()
  
    #Execute the functions
    

    #Import an update method
    clock = pygame.time.Clock()

    #Set some colors
    green = (0, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)

    #display screen
    screen = pygame.display.set_mode([800, 400])
    pygame.display.set_caption("Safety")

    #Create prompts
    tell = "Here are the possible options: type the respective number into the input box"
    prompt = "Type in 'quit' to end this program"
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(str(tell + "\n" + prompt), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (400 , 100)

    acceptableList = "(1)state list, (2)crime list, (3)murder, (4)assault, (5)sexual assault, quit"
    text_other = font.render(str(acceptableList) , True, green, blue)
    textRect_other = text_other.get_rect()
    textRect_other.center = (400, 150)

    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text = ''
      
    # create rectangle
    input_rect = pygame.Rect(320, 200, 140, 32)
  
    # color_active gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')
      
    # color_passive color of input box.
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
      
    active = False

    #print(start.functions())

    while True:
        for event in pygame.event.get():
            """
          # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            """
      
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                
                elif event.key == pygame.K_1:
                  user_text += event.unicode
                  thisText = Give_data_info.data_type.print_state_names()
                  words = font.render(thisText, True, green, blue)
                  wordsRect = words.get_rect()
                  wordsRect.center = (400, 150)
                  screen.blit(words, wordsRect)
                
                elif event.key == pygame.K_2:
                  user_text += event.unicode
                  thisText = Give_data_info.data_type.print_crime_types()
                  words = font.render(str(thisText), True, green, blue)
                  wordsRect = words.get_rect()
                  wordsRect.center = (400, 150)
                  screen.blit(words, wordsRect)

                elif event.key == pygame.K_3:
                  user_text += event.unicode
                  print_graphs_whole_country.plot_stats_country.print_stats_for_murder()
                  Open_interface.Open_window.run_the_app_murder_graph()
                
                elif event.key == pygame.K_4:
                  print_graphs_whole_country.plot_stats_country.print_stats_for_state_assault()
                  print(Open_interface.Open_window.run_the_app_assault_graph())

                elif event.key == pygame.K_5:
                  print_graphs_whole_country.plot_stats_country.print_stats_state_sexual_assault()
                  print(Open_interface.Open_window.run_the_app_sexual_assault_graph())

                elif event.key == pygame.K_KP_ENTER:
                    print(user_text)

                # Unicode standard is used for string
                else:
                    user_text += event.unicode
                    tell = "Please eneter as per given commands"
                    thesePrint = font.render(str(tell), True, green, blue)
                    thesePrintRect = thesePrint.get_rect()
                    thesePrintRect.center = (400, 150)
                    screen.blit(thesePrint, thesePrintRect)

          
        # it will set background color of screen
        screen.fill(red)
      
        if active:
            color = color_active
        else:
            color = color_passive
              
        # draw rectangle and argument passed which should be on screen
        pygame.draw.rect(screen, color, input_rect)
      
        text_surface = base_font.render(user_text, True, (255, 255, 255))
          
        # position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        #Output the prompts
        screen.blit(text, textRect)
        screen.blit(text_other, textRect_other)
        
          
        # set width of textfield so that text cannot get outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)
          
        # display.flip() will update only a portion of the screen to updated, not full area
        pygame.display.flip()
          
        # clock.tick(60) means that for every second at most 60 frames should be passed.
        clock.tick(60)

print(start.open())
"""
    https://www.codegrepper.com/code-examples/python/how+to+make+a+text+input+box+python+pygame
    https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
"""
mytitle = " - DISCORD COPY by ปุณณ์ แุณณ์"
from os import system
from pickle import REDUCE
system("title "+mytitle)
from pypresence import Presence
client_id = 'Your Account ID'
import discord
import asyncio
from pystyle import Colors, Colorate
from colorama import Fore, init, Style
import platform

re = Style.RESET_ALL
r = Fore.RED
g = Fore.BLUE
y = Fore.YELLOW
b = Fore.BLUE
m = Fore.MAGENTA
c = Fore.CYAN

if (__name__ == '__main__'):
    system('')


client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print((Colorate.Horizontal(Colors.rainbow,"""
    ██████╗ ██╗   ██╗███╗   ██╗███╗   ██╗
    ██╔══██╗██║   ██║████╗  ██║████╗  ██║
    ██████╔╝██║   ██║██╔██╗ ██║██╔██╗ ██║
    ██╔═══╝ ██║   ██║██║╚██╗██║██║╚██╗██║
    ██║     ╚██████╔╝██║ ╚████║██║ ╚████║
    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝
                                     
			(by ปุณณ์ ปุณณ์)""")))
token = input(f'{y} please enter token:\n > ')
print()
guild_s = input(f'{b}Please enter the ID discord to copy.:\n > ')
print()
guild = input(f'{r}:Please enter your discord ID.:\n > ')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token
print(re)

print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"{c}Logged In as : {client.user}")
    print(f"{c}Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print((Colorate.Horizontal(Colors.rainbow,"""
    ███████╗██╗███╗   ██╗██╗███████╗██╗  ██╗    
██╔════╝██║████╗  ██║██║██╔════╝██║  ██║    
█████╗  ██║██╔██╗ ██║██║███████╗███████║    
██╔══╝  ██║██║╚██╗██║██║╚════██║██╔══██║    
██║     ██║██║ ╚████║██║███████║██║  ██║    
╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝    
                                            
                                     
			(by ปุณณ์ ปุณณ์)""")))
    await asyncio.sleep(0)
    client.close()

def print_add(message):
    print(f'{g}[+]{re} {message}')

def print_delete(message):
    print(f'{r}[-]{re} {message}')

def print_warning(message):
    print(f'{r}[WARNING]{re} {message}')


def print_error(message):
    print(f'{r}[ERROR]{re} {message}')


class Clone:
    @staticmethod
    async def roles_delete(guild_to: discord.Guild):
            for role in guild_to.roles:
                try:
                    if role.name != f"{y}@everyone":
                        await role.delete()
                        print_delete(f"{y}Deleted Role: {role.name}")
                except discord.Forbidden:
                    print_error(f"{y}Error While Deleting Role: {role.name}")
                except discord.HTTPException:
                    print_error(f"{y}Unable to Delete Role: {role.name}{re}")

    @staticmethod
    async def roles_create(guild_to: discord.Guild, guild_from: discord.Guild):
        roles = []
        role: discord.Role
        for role in guild_from.roles:
            if role.name != f"{y}@everyone":
                roles.append(role)
        roles = roles[::-1]
        for role in roles:
            try:
                await guild_to.create_role(
                    name=role.name,
                    permissions=role.permissions,
                    colour=role.colour,
                    hoist=role.hoist,
                    mentionable=role.mentionable
                )
                print_add(f"{y}Created Role {role.name}")
            except discord.Forbidden:
                print_error(f"{y}Error While Creating Role: {role.name}")
            except discord.HTTPException:
                print_error(f"{y}Unable to Create Role: {role.name}{re}")

    @staticmethod
    async def channels_delete(guild_to: discord.Guild):
        for channel in guild_to.channels:
            try:
                await channel.delete()
                print_delete(f"{y}Deleted Channel: {channel.name}")
            except discord.Forbidden:
                print_error(f"{y}Error While Deleting Channel: {channel.name}")
            except discord.HTTPException:
                print_error(f"{y}Unable To Delete Channel: {channel.name}{re}")

    @staticmethod
    async def categories_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channels = guild_from.categories
        channel: discord.CategoryChannel
        new_channel: discord.CategoryChannel
        for channel in channels:
            try:
                overwrites_to = {}
                for key, value in channel.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                new_channel = await guild_to.create_category(
                    name=channel.name,
                    overwrites=overwrites_to)
                await new_channel.edit(position=channel.position)
                print_add(f"{y}Created Category: {channel.name}")
            except discord.Forbidden:
                print_error(f"{y}Error While Deleting Category: {channel.name}")
            except discord.HTTPException:
                print_error(f"{y}Unable To Delete Category: {channel.name}{re}")

    @staticmethod
    async def channels_create(guild_to: discord.Guild, guild_from: discord.Guild):
        channel_text: discord.TextChannel
        channel_voice: discord.VoiceChannel
        category = None
        for channel_text in guild_from.text_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_text.category.name:
                            break
                    except AttributeError:
                        print_warning(f"{y}Channel {channel_text.name} doesn't have any category!{re}")
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_text.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position,
                        topic=channel_text.topic,
                        slowmode_delay=channel_text.slowmode_delay,
                        nsfw=channel_text.nsfw)
                except:
                    new_channel = await guild_to.create_text_channel(
                        name=channel_text.name,
                        overwrites=overwrites_to,
                        position=channel_text.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"{y}Created Text Channel: {channel_text.name}")
            except discord.Forbidden:
                print_error(f"{y}Error While Creating Text Channel: {channel_text.name}")
            except discord.HTTPException:
                print_error(f"{y}Unable To Creating Text Channel: {channel_text.name}")
            except:
                print_error(f"{y}Error While Creating Text Channel: {channel_text.name}{re}")

        category = None
        for channel_voice in guild_from.voice_channels:
            try:
                for category in guild_to.categories:
                    try:
                        if category.name == channel_voice.category.name:
                            break
                    except AttributeError:
                        print_warning(f"{y}Channel {channel_voice.name} doesn't have any category!{re}")
                        category = None
                        break

                overwrites_to = {}
                for key, value in channel_voice.overwrites.items():
                    role = discord.utils.get(guild_to.roles, name=key.name)
                    overwrites_to[role] = value
                try:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position,
                        bitrate=channel_voice.bitrate,
                        user_limit=channel_voice.user_limit,
                        )
                except:
                    new_channel = await guild_to.create_voice_channel(
                        name=channel_voice.name,
                        overwrites=overwrites_to,
                        position=channel_voice.position)
                if category is not None:
                    await new_channel.edit(category=category)
                print_add(f"{y}Created Voice Channel: {channel_voice.name}")
            except discord.Forbidden:
                print_error(f"{y}Error While Creating Voice Channel: {channel_voice.name}")
            except discord.HTTPException:
                print_error(f"{y}Unable To Creating Voice Channel: {channel_voice.name}")
            except:
                print_error(f"{y}Error While Creating Voice Channel: {channel_voice.name}{re}")


    @staticmethod
    async def emojis_delete(guild_to: discord.Guild):
        for emoji in guild_to.emojis:
            try:
                await emoji.delete()
                print_delete(f"{y}Deleted Emoji: {emoji.name}")
            except discord.Forbidden:
                print_error(f"{y}Error While Deleting Emoji{emoji.name}")
            except discord.HTTPException:
                print_error(f"{y}Error While Deleting Emoji {emoji.name}{re}")

    @staticmethod
    async def emojis_create(guild_to: discord.Guild, guild_from: discord.Guild):
        emoji: discord.Emoji
        for emoji in guild_from.emojis:
            try:
                emoji_image = await emoji.url.read()
                await guild_to.create_custom_emoji(
                    name=emoji.name,
                    image=emoji_image)
                print_add(f"{y}Created Emoji {emoji.name}")
            except discord.Forbidden:
                print_error(f"{y}Error While Creating Emoji {emoji.name} ")
            except discord.HTTPException:
                print_error(f"{y}Error While Creating Emoji {emoji.name}{re}")

    @staticmethod
    async def guild_edit(guild_to: discord.Guild, guild_from: discord.Guild):
        try:
            try:
                icon_image = await guild_from.icon_url.read()
            except discord.errors.DiscordException:
                print_error(f"{y}Can't read icon image from {guild_from.name}")
                icon_image = None
            await guild_to.edit(name=f'{guild_from.name}')
            if icon_image is not None:
                try:
                    await guild_to.edit(icon=icon_image)
                    print_add(f"{y}Guild Icon Changed: {guild_to.name}")
                except:
                    print_error(f"{y}Error While Changing Guild Icon: {guild_to.name}")
        except discord.Forbidden:
            print_error(f"{y}Error While Changing Guild Icon: {guild_to.name}{re}")

client.run(token, bot=False)

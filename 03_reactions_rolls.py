import discord

class MyClient(discord.Client):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 1064871693186781225

    async def on_ready(self):
        print('yes im here')

    async def on_raw_reaction_add(self, payload):
        if payload.message_id != self.target_message_id:
            return
        
        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name =='😃':
            role = discord.utils.get(guild.roles, name='hello')
            await payload.member.add_roles(role)

        elif payload.emoji.name =='😞':
            role = discord.utils.get(guild.roles, name='chalo')
            await payload.member.add_roles(role)


        async def on_raw_reaction_remove(self, payload):
            if payload.message_id != self.target_message_id:
                return
        
            guild = client.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)

            if payload.emoji.name =='😃':
                role = discord.utils.get(guild.roles, name='hello')
                await member.remove_roles(role)

            elif payload.emoji.name =='😞':
                role = discord.utils.get(guild.roles, name='chalo')
                await member.remove_roles(role)

intents = discord.Intents.default()
intents.members = True


client = MyClient(intents=intents)
client.run('haha')